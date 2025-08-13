import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Virtual CI Specialist - Excel Test")

uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df)

    if "Loss Minutes" in df.columns and "Department" in df.columns:
        fig, ax = plt.subplots()
        df.groupby("Department")["Loss Minutes"].sum().plot(kind="bar", ax=ax)
        plt.ylabel("Loss Minutes")
        plt.title("Loss by Department")
        st.pyplot(fig)
    else:
        st.error("Excel must have 'Department' and 'Loss Minutes' columns.")

else:
    st.info("Please upload an Excel file to see results.")
