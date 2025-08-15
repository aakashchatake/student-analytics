import streamlit as st
import pandas as pd

st.title("📊 Student Quiz Analytics")

# 📥 Load quiz results
df = pd.read_csv("data/quiz_results.csv")
st.write("Columns in CSV:", df.columns.tolist())

# 🧮 Calculate total score and percentage
df['TotalScore'] = df[['Q1', 'Q2', 'Q3', 'Q4', 'Q5']].sum(axis=1)
df['Percentage'] = (df['TotalScore'] / 5) * 100  # Adjust denominator if needed

# 🎓 Assign grades
def assign_grade(pct):
    if pct >= 90:
        return 'A'
    elif pct >= 80:
        return 'B'
    elif pct >= 70:
        return 'C'
    elif pct >= 60:
        return 'D'
    else:
        return 'F'

df['Grade'] = df['Percentage'].apply(assign_grade)

# 🧾 Show raw and graded data
st.subheader("Graded Results")
st.dataframe(df)

# 📊 Grade distribution chart
st.subheader("Grade Distribution")
grade_counts = df['Grade'].value_counts().sort_index()
st.bar_chart(grade_counts)