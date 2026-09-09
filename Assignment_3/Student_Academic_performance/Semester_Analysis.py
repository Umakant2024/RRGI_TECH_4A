import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

data=np.array([
    [35,85,95],
    [85,75,90],
    [70,10,70]
])
subject=np.array(
    ['Physics','Chemistry','MAths']
)


total_marks=np.sum(data,axis=1)
avg=np.mean(data,axis=0)
# data=pd.read_csv('umakant_singh_semester_marks.csv')
# df=pd.DataFrame(data)
# semester=np.max(data)
# print(semester)
max=np.max(data,axis=1)
min=np.min(data,axis=1)
plt.subplot(3,2,1)
no_of_student=np.array([1,2,3])
plt.bar(subject,total_marks)
plt.subplot(3,2,2)
for i in range(3):
  plt.plot(no_of_student,data[i])
plt.subplot(3,2,3)
plt.bar(subject,max)
plt.subplot(3,2,4)
plt.bar(subject,min)
plt.subplot(3,2,5)
plt.plot(no_of_student,avg,linestyle='Dotted')
plt.show()