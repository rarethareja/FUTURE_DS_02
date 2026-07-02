import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(
    page_title="Customer Retention & Churn Dashboard",
    layout="wide"
)

#Dasboard Title and description
st.title("Customer Retention & Churn Dashboard")

st.markdown("""
This dashboard analyzes customer churn patterns and highlights the major factors
affecting customer retention using the Telco Customer Churn dataset.
""")

#Load the cleaned dataset
df = pd.read_csv("processed_data/Telco_Customer_Churn_Cleaned.csv")

# Sidebar filters
st.sidebar.header("Dashboard Filters")

contract_filter = st.sidebar.multiselect(
    "Select Contract Type",
    options=df["Contract"].unique(),
    default=df["Contract"].unique()
)

internet_filter = st.sidebar.multiselect(
    "Select Internet Service",
    options=df["InternetService"].unique(),
    default=df["InternetService"].unique()
)

# Apply filters
filtered_df = df[
    (df["Contract"].isin(contract_filter)) &
    (df["InternetService"].isin(internet_filter))
]

#Calculate Key Performance Indicators (KPIs)
total_customers = len(filtered_df)

churn_rate = (
    filtered_df["Churn"]
    .value_counts(normalize=True)["Yes"] * 100
)

avg_monthly =filtered_df["MonthlyCharges"].mean()

avg_tenure = filtered_df["tenure"].mean()

# Dashboard information
st.sidebar.markdown("---")

st.sidebar.subheader("Dashboard Summary")

st.sidebar.write(f"**Customers:** {len(filtered_df):,}")

st.sidebar.write(
    f"**Churn Rate:** "
    f"{filtered_df['Churn'].value_counts(normalize=True).get('Yes', 0) * 100:.2f}%"
)

st.sidebar.markdown("---")

st.sidebar.info(
    "Use the filters above to explore churn patterns "
    "across different customer segments."
)

#Display KPI cards
c1, c2, c3, c4 = st.columns(4)

c1.metric("Total Customers", f"{total_customers:,}")

c2.metric("Churn Rate", f"{churn_rate:.2f}%")

c3.metric("Avg Monthly Charges", f"${avg_monthly:.2f}")

c4.metric("Avg Customer Tenure", f"{avg_tenure:.1f} months")

# Customer churn distribution
churn_counts = (
    filtered_df["Churn"]
    .value_counts()
    .reset_index()
)

churn_counts.columns = ["Churn", "Count"]

fig = px.pie(
    churn_counts,
    names="Churn",
    values="Count",
    title="Customer Churn Distribution",
    hole=0.5,
    color="Churn",
    color_discrete_map={
        "Yes": "#EF553B",
        "No": "#00CC96"
    }
)

st.plotly_chart(fig, use_container_width=True, key='churn_distribution')

# Create two columns for visualizations
left_col, right_col = st.columns(2)

with left_col:

    contract_churn = (
        filtered_df.groupby("Contract")["Churn_Flag"]
        .mean()
        .mul(100)
        .round(2)
        .reset_index()
    )

    fig = px.bar(
        contract_churn,
        x="Contract",
        y="Churn_Flag",
        color="Contract",
        text="Churn_Flag",
        title="Churn Rate by Contract Type"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    st.plotly_chart(fig, use_container_width=True, key='contract_chart')

with right_col:

    internet_churn = (
        filtered_df.groupby("InternetService")["Churn_Flag"]
        .mean()
        .mul(100)
        .round(2)
        .reset_index()
    )

    fig = px.bar(
        internet_churn,
        x="InternetService",
        y="Churn_Flag",
        color="InternetService",
        text="Churn_Flag",
        title="Churn Rate by Internet Service"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    st.plotly_chart(fig, use_container_width=True, key='internet_chart')

# Create another row with two columns
left_col, right_col = st.columns(2)
with left_col:

    payment_churn = (
        filtered_df.groupby("PaymentMethod")["Churn_Flag"]
        .mean()
        .mul(100)
        .round(2)
        .reset_index()
    )

    fig = px.bar(
        payment_churn,
        x="PaymentMethod",
        y="Churn_Flag",
        color="PaymentMethod",
        text="Churn_Flag",
        title="Churn Rate by Payment Method"
    )

    fig.update_traces(
        texttemplate="%{text:.2f}%",
        textposition="outside"
    )

    fig.update_layout(
        xaxis_tickangle=-20
    )

    st.plotly_chart(fig, use_container_width=True, key='payment_chart')

with right_col:

    fig = px.histogram(
        filtered_df,
        x="tenure",
        color="Churn",
        nbins=30,
        title="Customer Tenure Distribution"
    )

    st.plotly_chart(fig, use_container_width=True, key='tenure_chart')

# Monthly charges comparison
fig = px.box(
    filtered_df,
    x="Churn",
    y="MonthlyCharges",
    color="Churn",
    title="Monthly Charges by Customer Churn Status"
)

st.plotly_chart(fig, use_container_width=True, key='monthly_charges')

# Total charges comparison
fig = px.box(
    filtered_df,
    x="Churn",
    y="TotalCharges",
    color="Churn",
    title="Total Charges by Customer Churn Status"
)

fig.update_layout(
    xaxis_title="Churn Status",
    yaxis_title="Total Charges ($)"
)

st.plotly_chart(fig, use_container_width=True, key='total_charges')

st.markdown("---")

st.header("Key Business Insights")

st.markdown("""
- Overall customer churn rate is **26.58%**.

- Month-to-month contracts experience the highest churn.

- Fiber optic customers have significantly higher churn than other internet service types.

- Electronic Check users exhibit the highest churn among payment methods.

- Most churn occurs during the early months of the customer lifecycle.

- Customers with higher monthly charges are more likely to churn.
""")

st.markdown("---")

st.caption(
    "Developed by Durlabh Thareja | "
    "Future Interns - Data Science & Analytics Task 2"
)