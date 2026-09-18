import pandas as pd
import matplotlib.pyplot as plt


# ============================================================
# 1. LOAD PROCESSED DATA
# ============================================================

file_path = "data/processed/ecommerce_transactions.csv"

df = pd.read_csv(file_path)

print("Dataset loaded successfully!")


# ============================================================
# 2. BASIC DATASET INFORMATION
# ============================================================

print("\nRows and columns:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nData types:")
print(df.dtypes)


# ============================================================
# 3. DATA QUALITY CHECKS
# ============================================================

print("\nMissing values:")
print(df.isnull().sum())

print("\nMissing value percentage:")
print(
    (df.isnull().sum() / len(df) * 100).round(2)
)

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nNegative quantities:")
print((df["Quantity"] < 0).sum())

print("\nZero prices:")
print((df["Price"] == 0).sum())

print("\nNegative prices:")
print((df["Price"] < 0).sum())


# ============================================================
# 4. DATA TYPE CONVERSION
# ============================================================

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["Customer ID"] = df["Customer ID"].astype("Int64")

# Create YearMonth for monthly analysis
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")


# ============================================================
# 5. TRANSACTION TYPE ANALYSIS
# ============================================================

print("\nTransaction types:")
print(df["TransactionType"].value_counts())


print("\nQuantity statistics:")
print(df["Quantity"].describe())


print("\nPrice statistics:")
print(df["Price"].describe())


print("\nTotal Amount statistics:")
print(df["TotalAmount"].describe())


# ============================================================
# 6. SALES VS CANCELLATIONS
# ============================================================

print("\nSales vs Cancellations:")

transaction_summary = (
    df.groupby("TransactionType")
    .agg(
        Transaction_Rows=("Invoice", "count"),
        Total_Quantity=("Quantity", "sum"),
        Total_Amount=("TotalAmount", "sum")
    )
)

print(transaction_summary)


# ============================================================
# 7. CREATE SALES DATAFRAME
# ============================================================

sales_df = df[
    df["TransactionType"] == "Sale"
].copy()


# ============================================================
# 8. MONTHLY SALES TREND
# ============================================================

print("\nMonthly Sales Trend:")

monthly_sales = (
    sales_df
    .groupby("YearMonth")["TotalAmount"]
    .sum()
)

print(monthly_sales)


# Monthly sales visualization
plt.figure(figsize=(12, 6))

monthly_sales.plot(kind="line")

plt.title("Monthly Gross Sales")
plt.xlabel("Month")
plt.ylabel("Gross Sales (£)")
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# ============================================================
# 9. TOP 10 COUNTRIES BY GROSS SALES
# ============================================================

print("\nTop 10 Countries by Gross Sales:")

country_sales = (
    sales_df
    .groupby("Country")["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(country_sales)


# Country visualization
plt.figure(figsize=(10, 6))

country_sales.sort_values().plot(kind="barh")

plt.title("Top 10 Countries by Gross Sales")
plt.xlabel("Gross Sales (£)")
plt.ylabel("Country")

plt.tight_layout()
plt.show()


# ============================================================
# 10. TOP 10 PRODUCTS BY GROSS SALES
# ============================================================

print("\nTop 10 Products by Gross Sales:")

product_sales = (
    sales_df
    .groupby(["StockCode", "Description"])["TotalAmount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(product_sales)


# Product visualization
product_sales_plot = product_sales.sort_values()

plt.figure(figsize=(10, 6))

product_sales_plot.plot(kind="barh")

plt.title("Top 10 Products by Gross Sales")
plt.xlabel("Gross Sales (£)")
plt.ylabel("Product")

plt.tight_layout()
plt.show()


# ============================================================
# 11. TOP 10 CUSTOMERS BY GROSS SALES
# ============================================================

print("\nTop 10 Customers by Gross Sales:")

customer_sales = (
    sales_df[
        sales_df["Customer ID"].notna()
    ]
    .groupby("Customer ID")
    .agg(
        Orders=("Invoice", "nunique"),
        Quantity=("Quantity", "sum"),
        Gross_Sales=("TotalAmount", "sum")
    )
    .sort_values(
        "Gross_Sales",
        ascending=False
    )
    .head(10)
)

print(customer_sales)


# ============================================================
# 12. REPEAT CUSTOMER ANALYSIS
# ============================================================

print("\nRepeat Customer Analysis:")

customer_orders = (
    sales_df[
        sales_df["Customer ID"].notna()
    ]
    .groupby("Customer ID")["Invoice"]
    .nunique()
)

total_customers = len(customer_orders)

repeat_customers = (
    customer_orders > 1
).sum()

one_time_customers = (
    customer_orders == 1
).sum()

repeat_customer_rate = (
    repeat_customers
    / total_customers
    * 100
)

print("Total customers:", total_customers)

print(
    "Repeat customers:",
    repeat_customers
)

print(
    "One-time customers:",
    one_time_customers
)

print(
    "Repeat customer rate:",
    round(repeat_customer_rate, 2),
    "%"
)


# ============================================================
# 13. AVERAGE ORDER VALUE (AOV)
# ============================================================

print("\nAverage Order Value (AOV):")

total_gross_sales = (
    sales_df["TotalAmount"].sum()
)

total_orders = (
    sales_df["Invoice"].nunique()
)

aov = (
    total_gross_sales
    / total_orders
)

print(
    "Gross Sales: £",
    round(total_gross_sales, 2)
)

print(
    "Total Orders:",
    total_orders
)

print(
    "Average Order Value: £",
    round(aov, 2)
)


# ============================================================
# 14. MONTHLY CANCELLATION RATE
# ============================================================

print("\nMonthly Cancellation Rate:")

monthly_transactions = (
    df
    .groupby(
        ["YearMonth", "TransactionType"]
    )
    .size()
    .unstack(fill_value=0)
)

# Make sure both columns exist
if "Sale" not in monthly_transactions.columns:
    monthly_transactions["Sale"] = 0

if "Cancellation" not in monthly_transactions.columns:
    monthly_transactions["Cancellation"] = 0


monthly_transactions["Total_Rows"] = (
    monthly_transactions["Sale"]
    + monthly_transactions["Cancellation"]
)


monthly_transactions["Cancellation_Rate"] = (
    monthly_transactions["Cancellation"]
    / monthly_transactions["Total_Rows"]
    * 100
)


print(
    monthly_transactions[
        [
            "Sale",
            "Cancellation",
            "Total_Rows",
            "Cancellation_Rate"
        ]
    ]
    .sort_values(
        "Cancellation_Rate",
        ascending=False
    )
)


# ============================================================
# 15. MONTHLY CANCELLATION RATE VISUALIZATION
# ============================================================

plt.figure(figsize=(12, 6))

monthly_transactions[
    "Cancellation_Rate"
].sort_index().plot(kind="line")

plt.title("Monthly Cancellation Rate")

plt.xlabel("Month")

plt.ylabel("Cancellation Rate (%)")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()


# ============================================================
# 16. FINAL SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("EDA COMPLETED SUCCESSFULLY")
print("=" * 60)

print("\nDataset rows:", len(df))

print(
    "Gross Sales: £",
    round(total_gross_sales, 2)
)

print(
    "Total Orders:",
    total_orders
)

print(
    "Average Order Value: £",
    round(aov, 2)
)

print(
    "Total Customers:",
    total_customers
)

print(
    "Repeat Customer Rate:",
    round(repeat_customer_rate, 2),
    "%"
)

print(
    "Cancellation Rows:",
    (df["TransactionType"] == "Cancellation").sum()
)

print("=" * 60)