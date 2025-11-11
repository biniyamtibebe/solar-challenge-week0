"""
MoonLight Energy Solutions – Solar Dashboard
Author: Biniyam Tibebe Solomon
Analytics Engineer | Economics Graduate
"""
# app/utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st  
  # YES

# === CONFIG (ONLY ONCE!) ===
warnings.filterwarnings('ignore')
sns.set(style="whitegrid", rc={"figure.figsize": (12, 6)})


def load_clean_country(path: str, country_name: str) -> pd.DataFrame:
    df = pd.read_csv(path, encoding='latin-1')
    df['Country'] = country_name
    return df


@st.cache_data
def load_all_data():
    try:
        benin = load_clean_country('../data/benin-malanville.csv', 'Benin')
        sierraleone = load_clean_country('../data/sierraleone_clean.csv', 'Sierra Leone')
        togo = load_clean_country('../data/togo_clean.csv', 'Togo')

        df = pd.concat([benin, sierraleone, togo], ignore_index=True)

        df['Country'] = df['Country'].replace({
            'sierraleone': 'Sierra Leone',
            'Togo': 'Togo',
            'Benin': 'Benin'
        })

        region_map = {
            'Benin': 'West Africa',
            'Sierra Leone': 'West Africa',
            'Togo': 'West Africa'
        }
        df['Region'] = df['Country'].map(region_map)

        if 'GHI' not in df.columns:
            ghi_cols = [c for c in df.columns if 'ghi' in c.lower() or 'hunger' in c.lower()]
            if ghi_cols:
                df['GHI'] = pd.to_numeric(df[ghi_cols[0]], errors='coerce')
            else:
                raise ValueError("No GHI column found")
        else:
            df['GHI'] = pd.to_numeric(df['GHI'], errors='coerce')

        df = df.dropna(subset=['GHI', 'Country-', 'Region'])
        return df

    except Exception as e:
        st.error(f"Data load error: {e}")
        return pd.DataFrame()


def create_ghi_boxplot(data, countries):
    filtered = data[data['Country'].isin(countries)]
    if filtered.empty:
        return None
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Country', y='GHI', data=filtered, palette="Set2")
    plt.title('GHI Distribution by Country', fontsize=16)
    plt.xlabel('Country')
    plt.ylabel('GHI Score')
    plt.xticks(rotation=15)
    return plt.gcf()


def get_top_regions_table(data, top_n=5):
    avg = (data.groupby(['Region', 'Country'])['GHI']
           .mean()
           .reset_index()
           .sort_values('GHI')
           .head(top_n))
    avg = avg.rename(columns={'GHI': 'Average GHI'})
    avg['Average GHI'] = avg['Average GHI'].round(2)
    return avg


# app/main.py
import streamlit as st
from utils import load_all_data, create_ghi_boxplot, get_top_regions_table
import os
from datetime import datetime
import pytz

# === CONFIG ===
st.set_page_config(page_title="West Africa GHI Dashboard", layout="wide")

# === TIME: Ethiopia (EAT) ===
eat = pytz.timezone('Africa/Addis_Ababa')
current_time = datetime.now(eat).strftime("%B %d, %Y %I:%M %p EAT")
st.caption(f"Updated: **{current_time}** | Ethiopia")

# === DATA ===
data = load_all_data()
if data.empty:
    st.stop()

# === HEADER ===
st.title("West Africa Hunger Index (GHI) Dashboard")
st.markdown("*Interactive analysis of **Benin**, **Sierra Leone**, and **Togo***")

# === SIDEBAR ===
st.sidebar.header("Filters")
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    options=sorted(data['Country'].unique()),
    default=['Benin']
)

# === 1. BOXPLOT ===
st.header("GHI Distribution by Country")
if selected_countries:
    fig = create_ghi_boxplot(data, selected_countries)
    if fig:
        st.pyplot(fig)
else:
    st.info("Select countries to view GHI distribution.")

# === 2. INDIVIDUAL GRAPHS ===
st.markdown("---")
st.subheader("Country-Specific GHI Trends")

graph_map = {
    'Benin': 'notebooks/data/benin_graph.png',
    'Sierra Leone': 'notebooks/data/sierraleone_graph.png',
    'Togo': 'notebooks/data/togo_graph.png'
}

shown = False
cols = st.columns(3)
col_idx = 0

for country in ['Benin', 'Sierra Leone', 'Togo']:
    if country in selected_countries and country in graph_map:
        path = graph_map[country]
        if os.path.exists(path):
            with cols[col_idx % 3]:
                st.image(path, caption=f"{country} GHI Trend", use_column_width=True)
            col_idx += 1
            shown = True
        else:
            st.warning(f"Missing: `{path}`")

if not shown and selected_countries:
    st.info("Graphs will appear when image files are available.")

# === 3. COMPARISON GRAPH ===
st.markdown("---")
st.subheader("Cross-Country GHI Comparison")
compare_path = 'notebooks/data/Compare_countries_graph.png'
if os.path.exists(compare_path):
    st.image(compare_path, caption="GHI Comparison: Benin vs Sierra Leone vs Togo", use_column_width=True)
else:
    st.warning("Comparison graph not found. Expected: `notebooks/data/Compare_countries_graph.png`")

# === 4. TOP REGIONS TABLE ===
st.markdown("---")
st.header("Top Performers (Lowest Average GHI)")
top_table = get_top_regions_table(data, top_n=10)
st.dataframe(top_table, use_container_width=True)

# === 5. INTERACTIVE FILTER ===
max_ghi = st.slider(
    "Filter by Maximum Average GHI",
    min_value=0.0,
    max_value=float(data['GHI'].max() or 100),
    value=30.0,
    step=0.5
)
filtered = top_table[top_table['Average GHI'] <= max_ghi]
st.dataframe(filtered, use_container_width=True, hide_index=True)

# === 6. DOWNLOAD BUTTON ===
csv = filtered.to_csv(index=False).encode()
st.download_button(
    label="Download Filtered Results (CSV)",
    data=csv,
    file_name=f"ghi_top_regions_{datetime.now(eat).strftime('%Y%m%d')}.csv",
    mime="text/csv",
    help="Download the current filtered top regions"
)

# === FOOTER ===
st.markdown("---")
st.markdown(
    """
    **Data**: Cleaned CSVs (`data/`) | **Visuals**: Matplotlib/Seaborn  
    **Graphs**: `notebooks/data/*.png` | **Deployed via Streamlit Community Cloud**
    """
)