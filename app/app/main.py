"""
MoonLight Energy Solutions – Solar Dashboard
Author: Biniyam Tibebe Solomon
Analytics Engineer | Economics Graduate
"""

import streamlit as st
import pandas as pd
from utils import load_data, create_boxplot, create_time_series, get_summary_stats
import plotly.express as px

# Set up Streamlit page configuration
st.set_page_config(page_title="MoonLight Solar", layout="wide")

# Dashboard title and author info
st.title("MoonLight Energy Solutions")
st.subheader("Cross-Country Solar Potential Dashboard")
st.markdown("**Analytics Engineer:** Biniyam Tibebe Solomon | Nov 2025")

# Sidebar for user controls
st.sidebar.header("Controls")
country = st.sidebar.selectbox("Select Country", ['Togo', 'Benin', 'Sierra Leone'])
metric = st.sidebar.radio("Metric", ['GHI', 'DNI', 'DHI'])

# Load data with a spinner
with st.spinner(f"Loading {country} data..."):
    df = load_data(country)
    df['Country'] = country

st.success(f"Loaded {len(df):,} observations from {country}")

# Layout for boxplot and time series
col1, col2 = st.columns(2)

with col1:
    st.plotly_chart(create_boxplot(df, metric), use_container_width=True)

with col2:
    st.plotly_chart(create_time_series(df, metric), use_container_width=True)

# Display summary statistics
st.markdown("### Summary Statistics")
st.dataframe(get_summary_stats(df), use_container_width=True)

# Ranking of countries based on Mean GHI
st.markdown("### Investment Ranking (Mean GHI)")
all_data = pd.concat([
    load_data('Togo').assign(Country='Togo'),
    load_data('Benin').assign(Country='Benin'),
    load_data('Sierra Leone').assign(Country='Sierra Leone')
])
ranking = all_data.groupby('Country')['GHI'].mean().sort_values(ascending=False)

# Create and display the ranking bar chart
fig = px.bar(
    x=ranking.index, 
    y=ranking.values,
    text=ranking.values.round(1),
    color=ranking.index,
    color_discrete_sequence=['gold', 'silver', '#CD7F32']
)
fig.update_layout(
    showlegend=False, 
    height=400,
    xaxis_title="Country", 
    yaxis_title="Mean GHI (W/m²)"
)
st.plotly_chart(fig, use_container_width=True)

# Strategic recommendation
st.markdown("### Strategic Recommendation")
st.success("""
**PRIORITIZE TOGO**  
→ Highest median GHI (260 W/m²)  
→ Lowest variability  
→ Statistically superior (p < 1e-100)  

**Next Step:** Deploy 50 MW pilot farm in Lomé, Togo – Q1 2026  
**Analytics by:** Biniyam Tibebe Solomon
""")