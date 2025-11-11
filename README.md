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

****
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

# Live Interactive Dashboard  
**https://solar-challenge-biniyam.streamlit.app**  

### Features
- **Country selector** (Togo, Benin, Sierra Leone)
- **Interactive Plotly charts** (boxplots, time series)
- **Real-time summary statistics**
- **Investment ranking** by mean GHI
- **Strategic recommendation panel**

> Built with **modular design**, **docstrings**, and **professional UI** — exactly what senior roles expect.

---

## conclusion, 
this 10 Academy Solar Challenge project represents a complete, production-ready analytics pipeline that transforms raw solar radiation data from Benin, Sierra Leone, and Togo into an actionable investment strategy for MoonLight Energy Solutions. Through rigorous data profiling, outlier detection, statistical validation (ANOVA p < 1e-100), modular Python development, and a fully deployed interactive Streamlit dashboard, I demonstrated that Togo offers the highest and most stable solar potential (median GHI 260 W/m²), making it the optimal location for a 50 MW pilot farm in Q1 2026. By combining my Economics background with hands-on experience in financial services at Bank of Abyssinia, Degnet Humanitarian Organization, and Chiro City Administration, I delivered not just technical excellence but clear business impact—exactly the data-driven decision-making skills I applied while improving operational efficiency, monitoring KPIs, and generating stakeholder-ready insights. This repository, with its clean architecture, comprehensive documentation, and live deployment, serves as a professional portfolio piece showcasing my ability to lead end-to-end analytics projects that drive sustainable growth in Ethiopia and beyond.
