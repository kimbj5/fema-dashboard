import streamlit as st
import plotly.express as px

st.title("FEMA Disaster Relief Dashboard")
st.write("Author: Benedict Kim")

df = pd.read_csv("https://drive.google.com/uc?id=1x8eId1u74uaMMO5KZijVmz6tpLC-xgei")

st.subheader("Data Preview")
st.write(df.head())

# Histogram
st.subheader("Histogram of Repair Amount")
fig_hist = px.histogram(df, x="repairAmount", nbins=30, title="Distribution of Repair Amounts")
st.plotly_chart(fig_hist)

st.markdown("**Insight:** There is a high frequency of claims with very low repair amounts, likely indicating minor damages or initial assessments. As the repair amount increases, the frequency of claims decreases significantly, showing a right-skewed distribution.")

# Boxplot
st.subheader("Boxplot: Repair Amount by TSA Eligibility")
fig_box = px.box(df, x="tsaEligible", y="repairAmount",
                 title="Repair Amount by TSA Eligibility",
                 labels={"tsaEligible": "TSA Eligible (1=Yes, 0=No)",
                         "repairAmount": "Repair Amount"})
st.plotly_chart(fig_box)

st.markdown("**Insight:** TSA-eligible households show higher median repair amounts compared to non-eligible households. A two-sample t-test confirmed this difference is statistically significant (t = 11.028, p < 0.001), suggesting that TSA eligibility is associated with greater damage costs.")
