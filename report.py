import pandas as pd
import os

file_path = "C:/Users/Jothiprakash/OneDrive/Documents/report.xlsx"

if not os.path.exists(file_path):
    print("File not found. Please check the path.")
else:
    df = pd.read_excel(file_path)
    print("File loaded successfully!")

    df.columns = df.columns.str.strip().str.upper()

    subjects = ["ACCOUNTS", "BOOM", "ECONOMICS", "OFFICE AUTOMATION"]

    for subject in subjects:
        df[subject] = pd.to_numeric(df[subject], errors='coerce').fillna(0)

    df["TOTAL"] = df[subjects].sum(axis=1)
    df["AVERAGE"] = df["TOTAL"] / len(subjects)

    def calculate_grade(avg):
        if avg >= 20:
            return 'A+'
        elif avg >= 15:
            return 'A'
        elif avg >= 10:
            return 'B'
        elif avg >= 5:
            return 'C'
        else:
            return 'F'

    df["GRADE"] = df["AVERAGE"].apply(calculate_grade)

    for _, row in df.iterrows():
        print(f"--- Report for {row['NAME OF THE STUDENTS']} ---")
        for subject in subjects:
            print(f"{subject}: {row[subject]}")
        print(f"Total: {row['TOTAL']}")
        print(f"Average: {row['AVERAGE']:.2f}")
        print(f"Grade: {row['GRADE']}")
        print("--------------\n")
