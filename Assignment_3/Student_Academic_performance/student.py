import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
# data=pd.read_csv('')
subject=np.array([
    [75,80,85],
    [80,75,95],
    [78,85,90]
])
SubName=np.array(['Physcis','Chemistry','Math'])
subjectName=np.array(['Alice','Bob','Kelly'])

total_marks=subject.sum(axis=1)
performance=subject.sum(axis=0)
avg_marks=subject.mean(axis=1)
percentage=(subject/total_marks)*100
print(percentage)
print(avg_marks)
print(total_marks)
plt.suptitle('Student_Report')
plt.subplot(2,2,1)
plt.bar(SubName,avg_marks,color='green')
plt.subplot(2,2,2)
plt.plot(subject,percentage)
plt.subplot(2,2,3)
plt.bar(subjectName,performance,color='yellow')
plt.subplot(2,2,4)
plt.plot(avg_marks,performance)
plt.show()
