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

