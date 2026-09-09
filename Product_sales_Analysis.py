import numpy as np
import pandas as pd
sales = np.array([ 
    [100, 120, 150], 
    [80, 100, 130], 
    [150, 160, 180], 
    [70, 90, 110], 
    [120, 140, 160] 
]) 
total_sales = np.sum(sales, axis=1)
Avg=np.mean(sales,axis=0)
best_product = np.argmax(total_sales)
worst_product = np.argmin(total_sales)
highest_monthly_sales = np.max(sales, axis=0)
lowest_monthly_sales = np.min(sales, axis=0)
monthly_total = np.sum(sales, axis=0)
std_dev = np.std(sales)
classification = np.where(Avg >= 120,"High", "Low")
df = pd.DataFrame({
    "Product": ["Product 1", "Product 2", "Product 3",
                "Product 4", "Product 5"],
    "Total Sales": total_sales,
    "Average Sales": average_sales
})
df["Status"]=classification
print(df)
sorted_df = df.sort_values(by="Total Sales", ascending=True)
print(sorted_df)