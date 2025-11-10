"""
Streamlit Dashboard Utilities
Author: Biniyam Tibebe Solomon
Date: 2025-11-10
"""

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

def load_data(country: str) -> pd.DataFrame:
    """
    Load cleaned CSV for the selected country.
    
    Parameters
    ----------
    country : str
        One of 'Benin', 'Sierra Leone', 'Togo'.
    
    Returns
    -------
    pd.DataFrame
        Cleaned data with Timestamp parsed.
    """
    path_map = {
        'Benin': '../data/benin_clean.csv',
        'Sierra Leone': '../data/sierraleone_clean.csv',
        'Togo': '../data/togo_clean.csv'
    }
    
    if country not in path_map:
        raise ValueError("Country must be one of 'Benin', 'Sierra Leone', or 'Togo'.")
    
    df = pd.read_csv(path_map[country])
    df['Timestamp'] = pd.to_datetime(df['Timestamp'])
    return df

def create_boxplot(df: pd.DataFrame, metric: str):
    """Create an interactive boxplot using Plotly."""
    fig = px.box(
        df, 
        y=metric, 
        color="Country",
        title=f"{metric} Distribution",
        labels={metric: f"{metric} (W/m²)"}
    )
    fig.update_layout(height=500)
    return fig

def create_time_series(df: pd.DataFrame, metric: str):
    """Create a daily average time series plot."""
    daily = df.set_index('Timestamp')[metric].resample('D').mean().reset_index()
    fig = px.line(
        daily, 
        x='Timestamp', 
        y=metric,
        title=f"Daily {metric} Trend",
        labels={metric: f"{metric} (W/m²)"}
    )
    fig.update_layout(height=500)
    return fig

def get_summary_stats(df: pd.DataFrame):
    """Return a formatted summary statistics table."""
    stats = df[['GHI', 'DNI', 'DHI']].agg(['mean', 'median', 'std']).round(1)
    stats.columns = ['Mean', 'Median', 'Standard Deviation']
    return stats