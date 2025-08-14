import streamlit as st
import pandas as pd
import plotly.express as px

# Page Config
st.set_page_config(page_title="Virtual CI Specialist", layout="wide")
st.title("📊 Virtual CI Specialist - Base App")

# File Upload
uploaded_file = st.file_uploader("Upload your Excel file", type=["xlsx"])

if uploaded_file:
    try:
        # Read Excel
        df = pd.read_excel(uploaded_file)

        # Check required columns
        required_cols = ["Date", "Department", "Reason", "Loss Minutes"]
        if not all(col in df.columns for col in required_cols):
            st.error(f"❌ Your file must have columns: {', '.join(required_cols)}")
        else:
            # Raw Data
            st.subheader("Raw Data")
            st.dataframe(df)

            # Daily Loss Calculation
            daily_loss = df.groupby("Date")["Loss Minutes"].sum().reset_index()
            daily_loss["OAE (%)"] = (1 - (daily_loss["Loss Minutes"] / 1440)) * 100

            st.subheader("Daily Losses & OAE")
            st.dataframe(daily_loss)

            # OAE Trend Chart
            fig_oae = px.line(daily_loss, x="Date", y="OAE (%)", title="OAE Trend")
            st.plotly_chart(fig_oae, use_container_width=True)

            # First-Level Pareto (by Department)
            pareto_dept = df.groupby("Department")["Loss Minutes"].sum().reset_index()
            pareto_dept = pareto_dept.sort_values("Loss Minutes", ascending=False)

            fig_pareto = px.bar(pareto_dept, x="Department", y="Loss Minutes",
                                title="Loss by Department", text="Loss Minutes")
            fig_pareto.update_traces(texttemplate='%{text}', textposition='outside')
            st.plotly_chart(fig_pareto, use_container_width=True)

            # Auto Insight
            top_dept = pareto_dept.iloc[0]["Department"]
            top_loss = pareto_dept.iloc[0]["Loss Minutes"]
            st.info(f"💡 Top loss contributor this period: **{top_dept}** with {top_loss} minutes lost.")

    except Exception as e:
        st.error(f"⚠️ Error reading file: {e}")

else:
    st.warning("Please upload your Excel file to start analysis.")
