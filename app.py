import streamlit as st
import pandas as pd

# ---------------------------
# PAGE CONFIG
# ---------------------------
st.set_page_config(page_title="E-commerce Dashboard", layout="wide")

# ---------------------------
# LOAD DATA
# ---------------------------
df = pd.read_csv("ecommerce.csv")

# Clean columns
df.columns = df.columns.str.strip()

# Convert dates
df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

# Feature engineering
df['Revenue'] = df['Quantity'] * df['UnitPrice']
df['Date'] = df['InvoiceDate'].dt.date
df['Month'] = df['InvoiceDate'].dt.to_period('M')

# Handle returns
df['IsReturn'] = df['Quantity'] < 0

# ---------------------------
# SIDEBAR FILTERS
# ---------------------------
st.sidebar.header("Filters")

start_date = st.sidebar.date_input("Start Date", df['Date'].min())
end_date = st.sidebar.date_input("End Date", df['Date'].max())

country = st.sidebar.selectbox(
    "Select Country",
    ["All"] + sorted(df['Country'].dropna().unique())
)

# Apply filters
filtered_df = df[
    (df['Date'] >= start_date) &
    (df['Date'] <= end_date)
].copy()

if country != "All":
    filtered_df = filtered_df[filtered_df['Country'] == country]

# Remove missing customers for analysis
filtered_df = filtered_df.dropna(subset=['CustomerID'])

# ---------------------------
# KPIs
# ---------------------------
total_revenue = filtered_df[filtered_df['Quantity'] > 0]['Revenue'].sum()
returns = filtered_df[filtered_df['Quantity'] < 0]['Revenue'].sum()
total_orders = filtered_df['InvoiceNo'].nunique()
avg_order_value = total_revenue / total_orders if total_orders > 0 else 0
unique_customers = filtered_df['CustomerID'].nunique()

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Revenue", f"${total_revenue:,.0f}")
col2.metric("Orders", total_orders)
col3.metric("Avg Order", f"${avg_order_value:,.0f}")
col4.metric("Customers", unique_customers)
col5.metric("Returns", f"${abs(returns):,.0f}")

# ---------------------------
# TITLE
# ---------------------------
st.title("🛒 E-commerce Sales Performance Dashboard")

# ---------------------------
# CHARTS LAYOUT
# ---------------------------

# Row 1
col1, col2 = st.columns(2)

with col1:
    st.subheader("Revenue Over Time")
    daily_sales = filtered_df.groupby('Date')['Revenue'].sum()
    st.line_chart(daily_sales)

with col2:
    st.subheader("Top Products")
    top_products = (
        filtered_df.groupby('Description')['Revenue']
        .sum()
        .sort_values(ascending=False)
        .head(10)
    )
    st.bar_chart(top_products)

# Row 2
col3, col4 = st.columns(2)

with col3:
    st.subheader("Revenue by Country")
    country_sales = filtered_df.groupby('Country')['Revenue'].sum()
    st.bar_chart(country_sales)

with col4:
    st.subheader("Monthly Revenue")
    monthly_sales = filtered_df.groupby('Month')['Revenue'].sum()
    st.line_chart(monthly_sales)

# ---------------------------
# CUSTOMER SEGMENTATION
# ---------------------------
st.subheader("Customer Segmentation")

customer_value = (
    filtered_df.groupby('CustomerID')['Revenue']
    .sum()
)

def segment(x):
    if x > 5000:
        return "High Value"
    elif x > 1000:
        return "Medium Value"
    else:
        return "Low Value"

customer_segment = customer_value.apply(segment)
segment_counts = customer_segment.value_counts()

st.bar_chart(segment_counts)

# ---------------------------
# TOP CUSTOMERS
# ---------------------------
st.subheader("Top Customers")

top_customers = (
    filtered_df.groupby('CustomerID')['Revenue']
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

st.bar_chart(top_customers)

# ---------------------------
# ORDER VALUE DISTRIBUTION
# ---------------------------
st.subheader("Order Value Distribution")

order_size = (
    filtered_df.groupby('InvoiceNo')['Revenue']
    .sum()
)

st.line_chart(order_size.value_counts().sort_index())

# ---------------------------
# BUSINESS INSIGHT
# ---------------------------
top_country = (
    filtered_df.groupby('Country')['Revenue']
    .sum()
    .idxmax()
)

st.write(f"🌍 Top Market: {top_country}")

# ---------------------------
# DOWNLOAD BUTTON
# ---------------------------
st.download_button(
    label="Download Filtered Data",
    data=filtered_df.to_csv(index=False),
    file_name="filtered_data.csv",
    mime="text/csv"
)

# ---------------------------
# DATA TABLE
# ---------------------------
st.subheader("Filtered Data")
st.dataframe(filtered_df)

