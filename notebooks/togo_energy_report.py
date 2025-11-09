# Report Generation in VS Code

print("""
# Togo Solar and Meteorological Insights

## Summary of Findings

1. **Irradiance Patterns Throughout the Year**:
   - The Global Horizontal Irradiance (GHI), Direct Normal Irradiance (DNI), and Diffuse Horizontal Irradiance (DHI) data illustrates a consistent irradiance pattern throughout the year, with peaks indicating optimal solar energy generation periods.

2. **Correlations Among Key Metrics**:
   - The correlation analysis reveals strong relationships between GHI, DNI, and DHI, with GHI having a notable positive correlation with temperature (Tamb) and a negative correlation with relative humidity (RH). This indicates that higher temperatures tend to enhance solar irradiance.

3. **Impact of Environmental Factors on Solar Efficiency**:
   - Box plots for temperature and humidity show that while temperatures generally remain within a favorable range for solar efficiency, humidity levels can vary significantly, potentially impacting overall performance.

4. **Recommendations for Solar Energy Deployment**:
   - It is recommended to focus on solar installations in areas with consistently high GHI and lower humidity levels to maximize energy generation potential.

## Graphs and Visualizations

### 1. Daily Solar Irradiance – Togo
![Daily Solar Irradiance](path_to_daily_solar_graph.png)
- This graph displays daily GHI, DNI, and DHI throughout the year, illustrating the trends and peaks in irradiance.

### 2. Correlation Heatmap
![Correlation Heatmap](path_to_correlation_heatmap.png)
- A heatmap showing correlations between solar metrics, highlighting the strong relationships that can inform energy production strategies.

### 3. Temperature (Tamb) and Humidity (RH) Box Plots
![Temperature and Humidity Box Plots](path_to_boxplots.png)
- Box plots visualizing the distributions of temperature and humidity, indicating their ranges and any potential outliers.

### 4. GHI vs Temperature – Bubble Size for Relative Humidity
![GHI vs Temperature](path_to_ghi_vs_temperature_graph.png)
- A scatter plot showing the relationship between GHI and temperature, with bubble size representing relative humidity, emphasizing how these factors interact.

### 5. Wind Rose – Togo
![Wind Rose](path_to_wind_rose_graph.png)
- A wind rose chart illustrating the distribution of wind direction and speed, providing insights into local wind patterns that may affect solar panel efficiency.

### 6. Distribution: GHI & Wind Speed
![Distribution: GHI & Wind Speed](path_to_distribution_graph.png)
- A histogram displaying the distributions of GHI and wind speed, offering a clear view of their frequency across the dataset.

### 7. Wind Speed vs GHI – Cleaning Events
![Wind Speed vs GHI](path_to_wind_speed_ghi_graph.png)
- A scatter plot showing the relationship between wind speed and GHI, with color indicating cleaning events, highlighting conditions under which panels perform best.

### 8. Cleaning Impact on ModA/ModB
![ModA and ModB: Clean vs Dirty](path_to_cleaning_impact_graph.png)
- A bar chart comparing average readings of ModA and ModB before and after cleaning events, demonstrating the significant boost in efficiency from regular maintenance.

## Conclusion
The insights and visualizations presented in this report underscore the significant potential for solar energy in Togo. By focusing on optimal conditions, such as high GHI and low humidity, alongside regular maintenance, stakeholders can maximize energy production and contribute to sustainable energy initiatives in the region.
""")