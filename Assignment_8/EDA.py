
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load cleaned dataset
df = pd.read_csv("cleaned_car_data.csv")

# Display basic information
print("Dataset Shape:", df.shape)

print("\nAverage Selling Price:")
print(df["selling_price_lakh"].mean())

print("\nAverage Price by Brand:")
print(
    df.groupby("brand")["selling_price_lakh"]
    .mean()
    .sort_values(ascending=False)
)

# 1. Distribution of car prices
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x="selling_price_lakh", kde=True)

plt.title("Distribution of Car Selling Prices")
plt.xlabel("Selling Price (Lakhs)")
plt.ylabel("Number of Cars")
plt.tight_layout()
plt.show()

# 2. Car manufacturing year vs price
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="year",
    y="selling_price_lakh"
)

plt.title("Manufacturing Year vs Selling Price")
plt.xlabel("Manufacturing Year")
plt.ylabel("Selling Price (Lakhs)")
plt.tight_layout()
plt.show()

# 3. Kilometers driven vs price
plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="km_driven",
    y="selling_price_lakh"
)

plt.title("Kilometers Driven vs Selling Price")
plt.xlabel("Kilometers Driven")
plt.ylabel("Selling Price (Lakhs)")
plt.tight_layout()
plt.show()

# 4. Average price by brand
brand_prices = (
    df.groupby("brand")["selling_price_lakh"]
    .mean()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 5))
brand_prices.plot(kind="bar")

plt.title("Average Selling Price by Brand")
plt.xlabel("Car Brand")
plt.ylabel("Average Selling Price (Lakhs)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
