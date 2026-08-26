import numpy as np
import pandas as pd
temperature = np.array([ 
    [32, 34, 35, 33, 31], 
    [28, 30, 31, 29, 27], 
    [35, 36, 38, 37, 34], 
    [25, 27, 29, 28, 26] 
]) 
days=np.array(['Monday', 'Tuesday', 'Wednesday',' Thursday', ' Friday' ])
#Average Temperature of each city
Avg_city=np.mean(temperature,axis=1)
print(Avg_city)

#Maximum temprature recorded by each city
Maximum_temp=np.max(temperature,axis=1)
print(Maximum_temp)

#Minimun temperature 

Minimum_temp=np.min(temperature,axis=1)
print(Minimum_temp)

#Hottest day
Hot_day=np.max(temperature,axis=0)
print(Hot_day)

#Coldest day
Cold_day=np.min(temperature,axis=0)
print(Cold_day)

#Highest avg
highest_city = np.argmax(city_avg)
print(highest_city)

above_30 = Avg_city > 30
print(np.where(above_30[0]+1))

std_dev = np.std(temperature)
print(std_dev)

df = pd.DataFrame(
    temperature,
    columns=days
)

print(df)