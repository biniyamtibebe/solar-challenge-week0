import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
import os
warnings.filterwarnings('ignore')
sns.set(style="whitegrid", rc={"figure.figsize": (12, 6)})

def load_clean_country(path: str, country_name: str) -> pd.DataFrame:

    """
    Load a cleaned CSV and add country identifier.
    
    Parameters
    ----------
    path : str
        Relative path to the cleaned CSV file
    country_name : str
        Name of the country (benin, sierraleon, and togo)
    """
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(path, encoding='latin-1')
    
    # Add country column
    df['Country'] = country_name
    
    return df

# Load data for each country
benin = load_clean_country(r'..\data\benin_clean.csv', 'Benin')
sierraleone = load_clean_country(r'..\data\sierraleone_clean.csv', 'sierraleone')
togo = load_clean_country(r'..\data\togo_clean.csv', 'Togo')

df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)

# Print the shapes of the loaded DataFrames
print(f"Loaded: Benin {benin.shape}, SierraLeone {sierraleone.shape}, Togo {togo.shape}")
"""
    Returns
    -------
    pd.DataFrame
        DataFrame with an added 'Country' column and parsed Timestamp.
    """
    # Initialize dictionary to hold country data
df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)
df_all['Timestamp'] = pd.to_datetime(df_all['Timestamp'])
print(f"Combined dataset: {df_all.shape}")
