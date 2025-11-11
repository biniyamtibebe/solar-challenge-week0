# app/utils.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import streamlit as st  # YES

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
        benin = load_clean_country('..\data/benin_clean.csv', 'Benin')
        sierraleone = load_clean_country('..\data/sierraleone_clean.csv', 'Sierra Leone')
        togo = load_clean_country('..\data/togo_clean.csv', 'Togo')

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

        df = df.dropna(subset=['GHI', 'Country', 'Region'])
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


