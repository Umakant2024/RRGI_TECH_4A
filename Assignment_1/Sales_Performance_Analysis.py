import numpy as np
import pandas as pd
sales=np.array([
    [12000, 15000, 18000], 
    [10000, 14000, 16000], 
    [18000, 20000, 22000], 
    [9000, 12000, 15000], 
    [15000, 17000, 19000] 
])
# columns: January, February, March
highestTotalSales=0
for i in range(len(sales)):
    total_sales = np.sum(sales[i], axis=1)
    if total_sales > highestTotalSales:
        highestTotalSales = total_sales

df=pd.DataFrame(
    {
        'total sales':total_sales,
        'average sales':np.mean(sales,axis=1),
        'highest sales in January':np.max(sales[0],axis=0),
        'highest sales in February':np.max(sales[1],axis=0),
        'highest sales in March':np.max(sales[2],axis=0),
        'lowest sales in January':np.min(sales[0],axis=0),
        'lowest sales in February':np.min(sales[1],axis=0),
        'lowest sales in March':np.min(sales[2],axis=0),
        'highest total sales':highestTotalSales

    }
)
print(df)