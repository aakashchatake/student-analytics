import streamlit as st
import pandas as pd
from PIL import Image

# Load scored results
df = pd.read_csv("reports/scored_results.csv")

st.set_page_config(page_title="Quiz Results Dashboard", layout="wide")
st.title("📊 Quiz Results Dashboard")
st.markdown("This dashboard summarizes student performance based on quiz scores.")

# Show DataFrame
st.subheader("📋 Scored Results")
st.dataframe(df)

# Grade Distribution
st.subheader("🎯 Grade Distribution")
grade_counts = df['Grade'].value_counts().sort_index()
st.bar_chart(grade_counts)

# Score Summary
st.subheader("📈 Score Summary")
st.write(df['Score'].describe())

# Show saved charts
st.subheader("🖼️ Visualizations")

col1, col2 = st.columns(2)

with col1:
    st.image(Image.open("reports/grade_pie_chart.png"), caption="Grade Pie Chart", use_column_width=True)

with col2:
    st.image(Image.open("reports/score_histogram.png"), caption="Score Histogram", use_column_width=True)

st.image(Image.open("reports/score_bell_curve.png"), caption="Score Bell Curve", use_column_width=True)
# ------------------- Add-ons -------------------

st.subheader("🧪 Filter and Export")

# Filter by Grade
selected_grades = st.multiselect(
    "Select Grades to View",
    options=sorted(df['Grade'].dropna().unique()),
    default=sorted(df['Grade'].dropna().unique())
)

filtered_df = df[df['Grade'].isin(selected_grades)]
st.dataframe(filtered_df)

# Download filtered results
st.download_button(
    label="📥 Download Filtered Results",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_results.csv",
    mime="text/csv"
)

# Student Count Summary
st.subheader("📊 Student Count Summary")
st.metric("Total Students", len(df))

for grade in sorted(grade_counts.index):
    st.metric(f"Grade {grade}", grade_counts[grade])