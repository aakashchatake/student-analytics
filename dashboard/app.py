import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("📊 Student Quiz Analytics")

# Load sample data
df = pd.read_csv("data/quiz_results.csv")

# Show raw data
st.subheader("Raw Results")
st.dataframe(df)

# Grade distribution
st.subheader("Grade Distribution")
fig, ax = plt.subplots()
df['Grade'].value_counts().plot(kind='bar', ax=ax)
st.pyplot(fig)