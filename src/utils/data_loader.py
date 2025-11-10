"""
Data loading utilities for solar challenge.
Author: Biniyam Tibebe Solomon
Date: 2025-11-10
"""
import pandas as pd

def load_clean_country(path: str, country_name: str) -> pd.DataFrame:
    """
    Load a cleaned CSV and add country identifier.
    
    Parameters
    ----------
    path : str
        Relative path to the cleaned CSV file
    country_name : str
        Name of the country (benin,sierraleon and togo)
        """
        
    # Load the CSV file into a DataFrame
    df = pd.read_csv(r'..\data\benin_clean.csv', encoding='latin-1')
    df= pd.read_csv(r'..\data\sierraleon_clean.csv', encoding='latin-1')
    df=pd.read_csv(r'..data\togo_clean.csv', encoding='latin=1')
# Print the number of rows loaded
    print(f"Loaded {country_name}: {df.shape[0]:,} rows")

  
    """
    Returns
    -------
    pd.DataFrame
        DataFrame with an added 'Country' column and parsed Timestamp.
    """
    # Initialize dictionary to hold country data
    country_data = {}
    df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)
    
    # Add country identifier and convert Timestamp to datetime
    df_all = pd.concat([benin, sierraleone, togo], ignore_index=True)
    df_all['Timestamp'] = pd.to_datetime(df_all['Timestamp'])
    print(f"Combined dataset: {df_all.shape}")
    
    # Store the modified DataFrame in the dictionary
    country_data[country_name] = df
    
    return df  # Return the modified DataFrame  


