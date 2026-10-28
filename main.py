import numpy as np
import pandas as pd

# Load dataset
df = pd.read_csv("students.csv")

# Function to calculate grade
def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


# Function to check pass or fail
def check_result(row):
    if (
        row["Python"] >= 40
        and row["Maths"] >= 40
        and row["AI"] >= 40
    ):
        return "Pass"
    return "Fail"


# Calculate total marks
df["Total"] = df[["Python", "Maths", "AI"]].sum(axis=1)

# Calculate average using NumPy
df["Average"] = np.round(
    df[["Python", "Maths", "AI"]].mean(axis=1), 2
)

# Assign grades using a loop
grades = []

for average in df["Average"]:
    grades.append(calculate_grade(average))

df["Grade"] = grades

# Calculate pass/fail result
df["Result"] = df.apply(check_result, axis=1)

# Display student report
print("\n===== STUDENT PERFORMANCE REPORT =====\n")

print(
    df[
        ["Student_ID", "Name", "Total", "Average", "Grade", "Result"]
    ].to_string(index=False)
)

# Overall statistics
print("\n===== RESULT SUMMARY =====")
print("Total Students:", len(df))
print("Students Passed:", (df["Result"] == "Pass").sum())
print("Students Failed:", (df["Result"] == "Fail").sum())
print("Class Average:", round(df["Average"].mean(), 2))
print("Highest Average:", df["Average"].max())
print("Lowest Average:", df["Average"].min())

# Step 4: Subject-wise Performance Analysis

subjects = ["Python", "Maths", "AI"]

print("\n===== SUBJECT-WISE ANALYSIS =====")

for subject in subjects:
    print(f"{subject} Average:", round(df[subject].mean(), 2))
    print(f"{subject} Highest Marks:", df[subject].max())
    print(f"{subject} Lowest Marks:", df[subject].min())

# Find the best-performing subject
subject_averages = df[subjects].mean()
best_subject = subject_averages.idxmax()

print("\nBest Performing Subject:", best_subject)

# Step 4.2: Top 5 Students

print("\n===== TOP 5 STUDENTS =====")

top_students = df.sort_values(
    by="Average", ascending=False
).head(5)

print(
    top_students[
        ["Student_ID", "Name", "Average", "Grade"]
    ].to_string(index=False)
)

# STEP 5: ATTENDANCE ANALYSIS

print("\n===== ATTENDANCE ANALYSIS =====")

# Calculate average attendance
average_attendance = df["Attendance"].mean()

print("Class Average Attendance:", round(average_attendance, 2), "%")

# Find students with attendance below 75%
low_attendance = df[df["Attendance"] < 75]

print("\nStudents with Attendance Below 75%:")

print(
    low_attendance[
        ["Student_ID", "Name", "Attendance"]
    ].to_string(index=False)
)

print("\nTotal Students with Low Attendance:", len(low_attendance))

# Find student with highest attendance
highest_attendance = df.loc[df["Attendance"].idxmax()]

print("\nHighest Attendance Student:", highest_attendance["Name"])
print("Attendance:", highest_attendance["Attendance"], "%")

# STEP 6: SAVE FINAL REPORT

df.to_csv("student_report.csv", index=False)

print("\n===== REPORT SAVED =====")
print("Final report saved as student_report.csv")
print("Total records saved:", len(df))