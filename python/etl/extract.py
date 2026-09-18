import pandas as pd

file_path = "data/raw/online_retail_II.xlsx"

# Check Excel sheets
excel_file = pd.ExcelFile(file_path)

print("Excel sheets:")
print(excel_file.sheet_names)

# Load both sheets
df_2009_2010 = pd.read_excel(
    file_path,
    sheet_name="Year 2009-2010"
)

df_2010_2011 = pd.read_excel(
    file_path,
    sheet_name="Year 2010-2011"
)

# Combine both sheets
df = pd.concat(
    [df_2009_2010, df_2010_2011],
    ignore_index=True
)

print("\nDataset loaded successfully!")

print("\nRows and columns:")
print(df.shape)

print("\nFirst 5 rows:")
print(df.head())

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nQuantity statistics:")
print(df["Quantity"].describe())

print("\nPrice statistics:")
print(df["Price"].describe())

print("\nNegative quantities:")
print((df["Quantity"] < 0).sum())

print("\nZero quantities:")
print((df["Quantity"] == 0).sum())

print("\nNegative prices:")
print((df["Price"] < 0).sum())

print("\nZero prices:")
print((df["Price"] == 0).sum())

print("\nNegative quantity examples:")
print(
    df[df["Quantity"] < 0][
        ["Invoice", "StockCode", "Description", "Quantity", "Price", "Customer ID"]
    ].head(10)
)

print("\nInvoices starting with C:")
print(df["Invoice"].astype(str).str.startswith("C").sum())

print("\nNegative quantity with C invoice:")
print(
    (
        (df["Quantity"] < 0)
        & (df["Invoice"].astype(str).str.startswith("C"))
    ).sum()
)