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
        plt.show()

# Example usage
if __name__ == "__main__":
    # Load your data here (replace with your actual data loading code)
    df_all = pd.read_csv('path/to/your/data.csv', encoding='latin-1')
    
    metrics = ['GHI', 'DNI', 'DHI']
    plot_metric_distribution(df_all, metrics)
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
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    # Assume df_all is already defined and loaded with the necessary data
    plot_ranking_bar_chart(df_all, 'GHI')