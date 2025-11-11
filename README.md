 # solar-challenge-week1

**Overview**

This project is part of the 10 Academy's AIM Week 0 Challenge. The goal is to prepare and analyze solar energy data from multiple countries to support region-ranking and decision-making tasks in renewable energy deployment. The work is divided into structured tasks. This README outlines the steps and deliverables completed for Task 1 and Task 2.


## ✅ Task 1: Git & Project Setup

**Objective**

  To set up a proper version-controlled project workspace using Git and GitHub for collaborative and organized development.

***Steps Completed***

    ✅ Initialized Git repository
    ✅ Created .gitignore to exclude unnecessary files (e.g., virtual environments, CSVs, notebook checkpoints)
    ✅ Set up Python virtual environment (venv) and installed required packages listed in requirements.txt
    ✅ Created development branches for each task and feature
    ✅ Successfully merged branches and maintained a clean commit history
    ✅ Pushed project to GitHub

## ## ✅ Task 2: Data Profiling, Cleaning & Exploratory Data Analysis (EDA)

### Objective

To profile, clean, and explore the solar dataset of each country to prepare it for downstream analysis and modeling.

### Countries Analyzed
- Benin
- Sierra Leone
- Togo

Each country has its own notebook and cleaned dataset stored locally under the `data/` folder.

---

1. **Branch Creation**
   - Created a dedicated branch for each country (e.g., `eda-sirraleone`)

2. **Notebook Analysis**
   - Notebooks: `benin_eda`,`sirraleone_eda.ipynb`, `togo_eda.ipynb`

3. **Data Profiling**
   - Used `df.describe()` to generate summary statistics
   - Used `df.isna().sum()` to report missing values
   - Flagged columns with more than 5% null values

4. **Data Cleaning**
   - Identified outliers using Z-score method (|Z| > 3)
   - Imputed missing values using median where applicable
   - Exported cleaned datasets to `data/<country>_clean.csv`

5. **Exploratory Data Analysis (EDA)**
   - Time series plots of GHI, DNI, DHI, and Tamb
   - Distribution and outlier analysis for sensor and wind readings
   - Correlation matrix heatmaps
   - Scatter plots to analyze environmental relationships
   - Bubble chart to examine GHI vs Tamb with RH or BP
   - Wind rose plots and histograms for key variables

6. **Cleaning Impact Analysis**
   - Compared ModA and ModB before and after cleaning
   - Grouped and visualized data based on cleaning flags
 ---
 
### ✅ Task 3: Cross-Country Comparison
**Objective**  
To synthesize the cleaned datasets from Benin, Sierra Leone, and Togo to identify relative solar potential and key differences across countries.

**Branch**: `compare-countries`  
**Notebook**: `compare_countries.ipynb`

**Key Steps Performed**  
- **Data Loading**  
  - Loaded cleaned CSVs (`data/benin_clean.csv`, `data/sierraleone_clean.csv`, `data/togo_clean.csv`)  
  - Combined datasets with a 'Country' column for unified analysis  
- **Metric Comparison**  
  - Created side-by-side boxplots for GHI, DNI, and DHI, colored by country  
  - Generated a summary table comparing mean, median, and standard deviation of GHI, DNI, DHI across countries  
- **Statistical Testing**  
  - Performed Kruskal-Wallis test on GHI to assess significant differences (p-value reported)  
- **Key Observations**  
  - Summarized findings in a markdown cell with 3 bullet points highlighting actionable insights (e.g., highest GHI, variability)  
- **Bonus Visualization**  
  - Created a bar chart ranking countries by average GHI 
- **Git Hygiene**  
  - Committed changes with message: `Completed Task 3: Cross-country comparison with boxplots, summary table, and statistical testing`  
  - Ensured `data/` folder remains ignored in `.gitignore`  

**Deliverables**  
- Notebook: `compare_countries.ipynb`  
- Summary table CSV: `data/summary_stats.csv`  
- Visuals: Boxplots and bar chart for GHI, DNI, DHI  

**KPIs Achieved**  
- Included all three countries in plots  
- Correctly reported p-values from statistical testing  
- Provided relevant, actionable insights in markdown  
- Generated a summary table with mean, median, and standard deviation

----

## Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/abmoh4219/solar-challenge-week1.git
   cd solar-challenge-week1
2. **Set up virtual environment**:
   ``` bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows Git Bash
   pip install -r requirements.txt

3. **Folder Structure**:
    ```bash
    -src/: Source code

    -notebooks/: Jupyter notebooks for EDA

    -tests/: Unit tests

    -scripts/: Utility scripts

    -data/: Data files (ignored in .gitignore)

---

### ✅ Task 4: Live Interactive Dashboard
Explore the dashboard here: http://localhost:8503/

**Features**
-Country Selector: Choose from Togo, Benin, or Sierra Leone.
-Interactive Plotly Charts: Includes boxplots and time series visualizations.
-Real-Time Summary Statistics: Instant insights at your fingertips.
-Investment Ranking: Displays countries ranked by mean GHI.
-Strategic Recommendation Panel: Provides actionable insights.
-This dashboard is built with a modular design, complete docstrings, and a professional -UI—catering to the expectations of senior roles.

---

## Conclusion

  This 10 Academy Solar Challenge project is a complete, production-ready analytics pipeline that turns raw solar radiation data from Benin, Sierra Leone, and Togo into actionable insights for MoonLight Energy Solutions. I utilized data profiling, outlier detection, and statistical validation (ANOVA p < 1e-100) to establish that Togo has the highest and most stable solar potential (median GHI 260 W/m²), making it ideal for a 50 MW pilot farm in Q1 2026. My background in Economics and experience in financial services allowed me to deliver both technical excellence and significant business impact. This repository showcases my ability to lead end-to-end analytics projects, with clean architecture, comprehensive documentation, and a live Streamlit dashboard.

---
