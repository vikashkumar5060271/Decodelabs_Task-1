import pandas as pd

# Read CSV file
df =pd.read_csv("Dataset for Data Analytics - Sheet1.csv")

# 1. Display Basic Information
print("First 5 Rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

# 2. Remove Duplicate Rows
df = df.drop_duplicates()

# 3. Remove Duplicate Order IDs
if "OrderID" in df.columns:
    df = df.drop_duplicates(subset="OrderID")

# 4. Handle Missing Values

# Fill missing text values
if "CouponCode" in df.columns:
    df["CouponCode"] = df["CouponCode"].fillna("No Coupon")

# Fill missing numeric values with median
numeric_columns = df.select_dtypes(include=["int64", "float64"]).columns

for col in numeric_columns:
    df[col] = df[col].fillna(df[col].median())

# 5. Fix Date Format
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(
        df["Date"],
        errors="coerce"
    )

    # Remove rows with invalid dates
    df = df.dropna(subset=["Date"])

    # Convert date format
    df["Date"] = df["Date"].dt.strftime("%Y-%m-%d")

# 6. Clean Text Columns
text_columns = df.select_dtypes(include=["object"]).columns

for col in text_columns:
    df[col] = df[col].astype(str).str.strip()

# 7. Final Check 
print("\nRemaining Missing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows Remaining:")
print(df.duplicated().sum())

if "OrderID" in df.columns:
    print("\nDuplicate Order IDs Remaining:")
    print(df["OrderID"].duplicated().sum())

# 8. Save Cleaned Dataset
df.to_csv("Cleaned_Dataset.csv", index=False)

print("\nDataset cleaned successfully!")
print("Cleaned file saved as: Cleaned_Dataset.csv")