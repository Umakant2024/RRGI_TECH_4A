
import pandas as pd

df = pd.read_csv("used_car_price_data.csv")

print("Original Dataset Shape:", df.shape)

# 1. Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# 2. Check duplicate records
print("\nDuplicate Rows:", df.duplicated().sum())

# 3. Remove duplicate records
df = df.drop_duplicates()

# 4. Remove rows with missing target prices
df = df.dropna(subset=["selling_price_lakh"])

# 5. Display dataset after cleaning
print("\nCleaned Dataset Shape:", df.shape)

# 6. Save the cleaned dataset
df.to_csv("cleaned_car_data.csv", index=False)

print("\nCleaned dataset saved successfully!")
