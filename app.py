import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page title
st.title("Test Deployment - Virtual CI Specialist")

# Dummy Data
data = {
    "Date": ["2025-08-10", "2025-08-11", "2025-08-12"],
    "Department": ["Maintenance", "Production", "Quality"],
    "Loss Minutes": [120, 90, 60]
}

df = pd.DataFrame(data)

st.subheader("Sample Data")
st.dataframe(df)

# Simple Chart
fig, ax = plt.subplots()
df.plot(kind="bar", x="Department", y="Loss Minutes", ax=ax)
st.pyplot(fig)

st.success("✅ This minimal app is running fine!")
