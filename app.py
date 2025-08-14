import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="CI Specialist - Test App", layout="wide")

st.title("📊 Virtual CI Specialist - Test App")

uploaded_file = st.file_uploader("Upload Excel file", type=["xlsx"])
if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.subheader("Uploaded Data")
    st.dataframe(df)

    if "Loss Minutes" in df.columns:
        fig = px.bar(df, x="Department", y="Loss Minutes", color="Reason",
                     title="Loss Minutes by Department & Reason", barmode="group")
        st.plotly_chart(fig, use_container_width=True)

        oae = 100 - (df["Loss Minutes"].sum() / (24 * 60) * 100)
        st.metric("OAE (%)", f"{oae:.2f}")
    else:
        st.error("Your Excel must contain 'Loss Minutes' column.")
else:
    st.info("Please upload an Excel file to get started.")
