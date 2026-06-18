# 🚢 Data Cleaning & Reporting Automation using Titanic Dataset

## 📌 Overview

This project automates the process of **data cleaning, report generation, and visualization** using the Titanic dataset. The workflow handles missing values, removes duplicate records, generates a detailed analytical report, and creates visual summaries automatically using Python.

---

## 🎯 Project Objective

The objective of this project is to automate data preprocessing and reporting workflows while gaining practical experience in:

* Data Cleaning
* Data Preprocessing
* Data Visualization
* Report Generation
* Workflow Automation

---

## ✨ Features

✔ Automated data cleaning and preprocessing

✔ Missing value detection and handling

✔ Duplicate record identification and removal

✔ Automated report generation

✔ Automated chart generation and visualization

✔ Export of cleaned dataset for further analysis

---

## 📊 Dataset

**Dataset:** Titanic Dataset

The dataset contains passenger information such as:

* Passenger ID
* Survival Status
* Passenger Class
* Name
* Gender
* Age
* Fare
* Ticket Details
* Cabin Information
* Embarkation Port

---

## 🧹 Data Cleaning Process

The following preprocessing steps were performed:

### Handling Missing Values

* Filled missing values in the **Age** column using the **Median**
* Filled missing values in the **Embarked** column using the **Mode**
* Replaced missing values in the **Cabin** column with **"Unknown"**

### Duplicate Removal

* Identified duplicate records
* Removed duplicate entries from the dataset

---

## 📈 Generated Outputs

The script automatically generates the following files inside the `output/` folder:

| File Name                        | Description                        |
| -------------------------------- | ---------------------------------- |
| Titanic_Cleaned.csv              | Cleaned dataset                    |
| Titanic_Detailed_Report.txt      | Detailed data analysis report      |
| Survival_Count.png               | Survival count visualization       |
| Gender_Distribution.png          | Gender distribution chart          |
| Passenger_Class_Distribution.png | Passenger class distribution chart |
| Age_Distribution.png             | Age distribution histogram         |

---

## 🛠 Technologies Used

* Python
* Pandas
* Matplotlib

---

## 📂 Project Structure

```text
data-cleaning-reporting-automation-titanic/
│
├── train.csv
├── Titanic_Automation.py
│
└── output/
    ├── Titanic_Cleaned.csv
    ├── Titanic_Detailed_Report.txt
    ├── Survival_Count.png
    ├── Gender_Distribution.png
    ├── Passenger_Class_Distribution.png
    └── Age_Distribution.png
```

---

## ⚙ Installation

Install the required libraries:

```bash
pip install pandas matplotlib
```

---

## ▶ How to Run

### Step 1

Download the Titanic dataset and place `train.csv` inside the project folder.

### Step 2

Open the project in Python IDLE, VS Code, PyCharm, or any Python IDE.

### Step 3

Run the script:

```bash
python Titanic_Automation.py
```

### Step 4

The cleaned dataset, report, and visualizations will be automatically generated inside the `output/` folder.

---

## 📷 Sample Outputs

The project generates:

* Survival Count Chart
* Gender Distribution Chart
* Passenger Class Distribution Chart
* Age Distribution Histogram
* Cleaned Dataset CSV
* Detailed Analysis Report

---

## 🎓 Learning Outcomes

Through this project, the following concepts were learned:

* Data Preprocessing
* Missing Value Handling
* Duplicate Data Removal
* Automated Report Generation
* Data Visualization using Matplotlib
* Workflow Automation using Python

---

## ✅ Conclusion

This project successfully demonstrates an automated data cleaning and reporting workflow using the Titanic dataset. By integrating preprocessing, reporting, and visualization into a single Python script, the project improves reporting efficiency and supports data-driven decision-making.

---
