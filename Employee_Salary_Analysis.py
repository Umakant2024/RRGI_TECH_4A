import numpy as np
import pandas as pd
salary1 = np.array([
 [25000, 2, 80],
 [45000, 5, 90],
 [30000, 3, 75],
 [60000, 8, 95],
 [35000, 4, 85]
])
salary2=salary1.T
for i in range(len(salary2)):
    
    max_salary=0
    min_salary=1000000
    for j in range(len(salary2[i])):
        if(max_salary<salary2[i][j]):
            max_salary=salary2[i][j]
        if(min_salary>salary2[i][j]):
            min_salary=salary2[i][j]
    break        
average_salary=np.mean(salary2[i])        
if(average_salary>=40000):
      print("Employee ",i+1," has average salary above 40000")    

df=pd.DataFrame({
    'Average_salary':np.mean(salary1[0],axis=0),
    'Maximum_salary':max_salary,
    'Minimum_salary':min_salary,
    'Average_experience':np.mean(salary1[1],axis=0),
    'Performance_score above 80':np.where(salary1[2]>=80, "Yes", "No"),
    'Standard_deviation_salary':np.std(salary1[0],axis=0),
    'Salary_classification':np.where(salary1[0]>=40000, "High", "Low")
    
})
print(df)