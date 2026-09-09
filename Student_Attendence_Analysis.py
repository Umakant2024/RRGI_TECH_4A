import numpy as np
import pandas as pd
attendance = np.array([ 
    [90, 85, 95, 88], 
    [75, 80, 70, 78], 
    [95, 92, 98, 96], 
    [65, 70, 72, 68], 
    [85, 88, 90, 87] 
])
Subject=np.array(['Python','Java','SQL','ML'])
Avg=np.mean(attendance,axis=1)
Avg_Subject=np.mean(attendance,axis=0)
max_Attend_subject=np.max(attendance,axis=0)
min_Attend_subject=np.min(attendance,axis=0)
for i in range(len(attendance)):
  if(Avg[i]>=80):
      print(i+1,'student having Attendance above 80')
std=np.std(attendance,axis=1)
Status=np.where(Avg>75,'Eligible','Not Eligible')
df = pd.DataFrame(
    attendance,
    columns=["Python", "Java", "SQL", "ML"]
)
df["Status"] = Status
print(df)