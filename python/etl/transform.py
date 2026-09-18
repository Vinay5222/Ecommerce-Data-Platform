import pandas as pd

file_path = "data/raw/online_retail_II.xlsx"

# Load both sheets
df_2009_2010 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010"
)

df_2010_2011 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

# Combine datasets
df = pd.concat(
    [df_2009_2010, df_2010_2011],
    ignore_index=True
)

print("Raw dataset:")
print(df.shape)

# Remove exact duplicate rows
df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df.shape)

# Remove rows with invalid negative prices
df = df[df["Price"] >= 0]

print("\nAfter removing negative prices:")
print(df.shape)

# Create transaction type
df["TransactionType"] = "Sale"

df.loc[
    df["Invoice"].astype(str).str.startswith("C"),
    "TransactionType"
] = "Cancellation"

# Create total amount
df["TotalAmount"] = df["Quantity"] * df["Price"]

# Convert Customer ID to nullable integer
df["Customer ID"] = df["Customer ID"].astype("Int64")

print("\nTransaction types:")
print(df["TransactionType"].value_counts())

print("\nFinal columns:")
print(df.columns.tolist())

print("\nSample transformed data:")
print(
    df[
        [
            "Invoice",
            "StockCode",
            "Description",
            "Quantity",
            "Price",
            "Customer ID",
            "TransactionType",
            "TotalAmount"
        ]
    ].head(10)
)

# Save transformed dataset
output_path = "data/processed/ecommerce_transactions.csv"

df.to_csv(
    output_path,
    index=False
)

print("\nTransformed dataset saved successfully!")
print(f"File: {output_path}")

# Verify saved CSV
df_check = pd.read_csv(output_path)

print("\nProcessed CSV verification:")
print("Rows:", len(df_check))
print("Columns:", len(df_check.columns))

print("\nColumns:")
print(df_check.columns.tolist())

print("\nMissing values:")
print(df_check.isnull().sum())