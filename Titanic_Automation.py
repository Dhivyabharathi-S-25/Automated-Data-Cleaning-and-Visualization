import pandas as pd
import matplotlib.pyplot as plt
import os

# Create output folder
os.makedirs("output", exist_ok=True)
print("Loading Titanic Dataset...")

# Load dataset
df = pd.read_csv("Titanic-Dataset.csv")

print("Dataset loaded successfully.")

# Store original information
original_shape = df.shape
missing_before = df.isnull().sum()
duplicates_before = df.duplicated().sum()

print("Cleaning and preprocessing data...")

# -------------------------------
# DATA CLEANING
# -------------------------------

df["Age"] = df["Age"].fillna(df["Age"].median())
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])
df["Cabin"] = df["Cabin"].fillna("Unknown")

df.drop_duplicates(inplace=True)

missing_after = df.isnull().sum()

# -------------------------------
# SAVE CLEANED DATASET
# -------------------------------

df.to_csv("output/Titanic_Cleaned.csv", index=False)

print("Generating reports and visualizations...")

# -------------------------------
# GENERATE DETAILED REPORT
# -------------------------------

with open("output/Titanic_Detailed_Report.txt", "w", encoding="utf-8") as report:

    report.write("=========================================\n")
    report.write(" TITANIC DATA CLEANING & REPORTING REPORT\n")
    report.write("=========================================\n\n")

    report.write("1. DATASET OVERVIEW\n")
    report.write("-------------------\n")
    report.write(f"Original Dataset Shape : {original_shape}\n")
    report.write(f"Cleaned Dataset Shape  : {df.shape}\n\n")

    report.write("2. MISSING VALUES BEFORE CLEANING\n")
    report.write("---------------------------------\n")
    report.write(missing_before.to_string())
    report.write("\n\n")

    report.write("3. MISSING VALUES AFTER CLEANING\n")
    report.write("--------------------------------\n")
    report.write(missing_after.to_string())
    report.write("\n\n")

    report.write("4. DUPLICATE RECORDS\n")
    report.write("--------------------\n")
    report.write(f"Duplicate Rows Found : {duplicates_before}\n\n")

    report.write("5. DATA TYPES\n")
    report.write("-------------\n")
    report.write(df.dtypes.to_string())
    report.write("\n\n")

    report.write("6. STATISTICAL SUMMARY\n")
    report.write("----------------------\n")

    report.write(f"Average Age      : {round(df['Age'].mean(), 2)}\n")
    report.write(f"Minimum Age      : {df['Age'].min()}\n")
    report.write(f"Maximum Age      : {df['Age'].max()}\n\n")

    report.write(f"Average Fare     : {round(df['Fare'].mean(), 2)}\n")
    report.write(f"Minimum Fare     : {df['Fare'].min()}\n")
    report.write(f"Maximum Fare     : {df['Fare'].max()}\n\n")

    report.write(f"Average Pclass   : {round(df['Pclass'].mean(), 2)}\n")
    report.write(f"Total Passengers : {len(df)}\n")
    report.write(f"Total Survivors  : {df['Survived'].sum()}\n")
    report.write(f"Survival Rate    : {round((df['Survived'].mean()*100), 2)}%\n\n")
    

    report.write("7. SURVIVAL ANALYSIS\n")
    report.write("--------------------\n")
    report.write(df["Survived"].value_counts().to_string())
    report.write("\n\n")

    report.write("8. GENDER DISTRIBUTION\n")
    report.write("----------------------\n")
    report.write(df["Sex"].value_counts().to_string())
    report.write("\n\n")

    report.write("9. PASSENGER CLASS DISTRIBUTION\n")
    report.write("-------------------------------\n")
    report.write(df["Pclass"].value_counts().to_string())
    report.write("\n\n")

    
# -------------------------------
# CHART 1
# -------------------------------

plt.figure(figsize=(6, 4))
df["Survived"].value_counts().plot(kind="bar")
plt.title("Survival Count")
plt.xlabel("Survived")
plt.ylabel("Number of Passengers")
plt.tight_layout()
plt.savefig("output/Survival_Count.png")
plt.close()

# -------------------------------
# CHART 2
# -------------------------------

plt.figure(figsize=(6, 6))
df["Sex"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.ylabel("")
plt.title("Gender Distribution")
plt.tight_layout()
plt.savefig("output/Gender_Distribution.png")
plt.close()

# -------------------------------
# CHART 3
# -------------------------------

plt.figure(figsize=(6, 4))
df["Pclass"].value_counts().plot(kind="bar")
plt.title("Passenger Class Distribution")
plt.xlabel("Passenger Class")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("output/Passenger_Class_Distribution.png")
plt.close()

# -------------------------------
# CHART 4
# -------------------------------

plt.figure(figsize=(7, 4))
plt.hist(df["Age"], bins=20)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("output/Age_Distribution.png")
plt.close()


print("\nAutomated data cleaning, report generation, and visualization completed successfully.")
