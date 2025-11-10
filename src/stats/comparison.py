"""
Statistical comparison across countries.
Author: Biniyam Tibebe Solomon
"""
from scipy import stats 
import pandas as pd


# -----------------------------------------------------
# 4. SUMMARY STATISTICS TABLE
# -----------------------------------------------------

import pandas as pd

def summary_table(df: pd.DataFrame, metrics: list) -> pd.DataFrame:
    """
    Generate a summary statistics table for specified metrics by country.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing solar metrics data, including 'Country' and specified metrics.
    metrics : list
        List of metric names (e.g., 'GHI', 'DNI', 'DHI') for which to calculate statistics.

    Returns
    -------
    pd.DataFrame
        A DataFrame containing the mean, median, and standard deviation for each metric by country.
    """
    stats_dict = {}
    
    for country in df['Country'].unique():
        subset = df[df['Country'] == country]
        stats_dict[country] = {
            metric: f"{subset[metric].mean():.1f} ({subset[metric].median():.1f}) ± {subset[metric].std():.1f}"
            for metric in metrics
        }
    
    # Create and return a DataFrame from the statistics dictionary
    return pd.DataFrame(stats_dict).T  # Transpose for better readability

# Example usage
if __name__ == "__main__":
    # Assume df_all is already defined and loaded with the necessary data
    metrics = ['GHI', 'DNI', 'DHI']  # Define which metrics to summarize
    summary = summary_table(df_all, metrics)
    
    # Display the summary table
    print(summary)

    # -----------------------------------------------------
# 5. STATISTICAL TESTING – ANOVA + KRUSKAL-WALLIS
# -----------------------------------------------------

import pandas as pd
from scipy import stats

def statistical_tests(df: pd.DataFrame, metric: str) -> tuple:
    """
    Perform ANOVA and Kruskal-Wallis tests on a specified metric.

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame containing solar metrics data, including 'Country' and the specified metric.
    metric : str
        The name of the metric to test (e.g., 'GHI').

    Returns
    -------
    tuple
        A tuple containing the p-values from the ANOVA and Kruskal-Wallis tests.
    """
    # Group data by country and extract the values for the specified metric
    groups = [group[metric].values for name, group in df.groupby('Country')]
    
    # Perform ANOVA (assumes normal distribution)
    f_stat, p_anova = stats.f_oneway(*groups)
    
    # Perform Kruskal-Wallis (non-parametric test)
    h_stat, p_kruskal = stats.kruskal(*groups)
    
    return p_anova, p_kruskal

# Example usage
if __name__ == "__main__":
    # Assume df_all is already defined and loaded with the necessary data
    ghi_anova, ghi_kruskal = statistical_tests(df_all, 'GHI')
    
    # Display the results
    print(f"GHI – ANOVA p-value: {ghi_anova:.2e}")
    print(f"GHI – Kruskal-Wallis p-value: {ghi_kruskal:.2e}")
    
    # Interpretation of results
    if ghi_anova < 0.05 or ghi_kruskal < 0.05:
        print("→ p < 0.05 → Differences between countries are STATISTICALLY SIGNIFICANT")
    else:
        print("→ p >= 0.05 → No statistically significant differences between countries")

        # -----------------------------------------------------
