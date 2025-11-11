
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
#-----------------------------------------------------



# 3. METRIC COMPARISON – BOXPLOTS
# -----------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_metric_distribution(df: pd.DataFrame, metrics: list) -> None:
    """
    Plot boxplots for given metrics by country.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing solar metrics data, including 'Country' and specified metrics.
    metrics : list
        List of metric names (e.g., 'GHI', 'DNI', 'DHI') to plot.

    Returns
    -------
    None
        This function displays boxplots for each metric.
    """
    for metric in metrics:
        plt.figure(figsize=(10, 6))
        sns.boxplot(data=df, x='Country', y=metric, palette='Set2')
        plt.title(f'{metric} Distribution by Country', fontsize=16, pad=20)
        plt.ylabel(f'{metric} (W/m²)')
        plt.xlabel('Country')
        plt.grid(True, alpha=0.3)
# Example usage
if __name__ == "__main__":
   
    metrics = ['GHI', 'DNI', 'DHI']
    
     #Show the plots
plt.tight_layout()
plt.savefig('../notebooks/compare_countries.ipynb', format='png', dpi=200)
plt.close()
plt.show()

# 6. RANKING BAR CHART (BONUS)
# -----------------------------------------------------

import matplotlib.pyplot as plt
import pandas as pd

def plot_ranking_bar_chart(df: pd.DataFrame, metric: str) -> None:
    """
    Plot a ranking bar chart for the average values of a specified metric by country.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing solar metrics data, including 'Country' and the specified metric.
    metric : str
        The name of the metric to rank (e.g., 'GHI').

    Returns
    -------
    None
        This function displays a bar chart ranking countries by the specified metric.
    """
    # Calculate mean values and sort them in descending order
    means = df.groupby('Country')[metric].mean().sort_values(ascending=False)

    # Create the bar chart
    plt.figure(figsize=(8, 5))
    bars = plt.bar(means.index, means.values, color=['gold', 'silver', 'chocolate'])
    plt.title(f'Average {metric} Ranking – Recommended Investment Order', fontsize=16, pad=20)
    plt.ylabel(f'Mean {metric} (W/m²)')
    plt.xlabel('Country')

    # Add value labels on the bars
    for bar in bars:
        height = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2., height + 5,
                 f'{height:.1f}', ha='center', va='bottom', fontsize=12, fontweight='bold')

    # Set y-axis limits and display grid
    plt.ylim(0, max(means.values) * 1.15)
    plt.grid(True, axis='y', alpha=0.3)
# Example usage
if __name__ == "__main__":
    # Assume df_all is already defined and loaded with the necessary data
    plot_ranking_bar_chart(df_all, 'GHI')
# Show the plots
plt.tight_layout()
plt.savefig('../notebooks/data/Compare_countries_graph.png', format='png', dpi=200)
plt.close()
plt.show()