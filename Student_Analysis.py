import numpy as np
import pandas as pd
marks=np.array([
    [85,80,90],
    [70,75,65],
    [70,75,65],
    [60,72,68],
    [80,85,90]
])
# # total sum and average of each student and each subject
# for i in range(len(marks)):
#     sum=0
#     average=0
#     max=0
#     min=1000
#     for j in range(len(marks[i])):
#         sum +=marks[i][j]
       
#     average=sum//3
#     if(average>=80):
#         print("Student ",i+1," has average above 80")    
#     print("Total marks of student ",i+1," is ",sum ," and Average",average,)  


# maximum and minimum marks of each student in specific subject
# for i in range(len(marks[0])):
#     max=0
#     min=1000
    
#     for j in range(len(marks)):
#         if(max<marks[j][i]):
#             max=marks[j][i]
#         if(min>marks[j][i]):
#             min=marks[j][i]    
#     print(" Maximum and Minimum Marks of Student ",i+1, "is", max,min)
transpose=marks.T
# for i in range(len(transpose)):
#     subsum=0
    
#     for j in range(len(transpose[i])):
#         subsum+=transpose[i][j]
#     if(i==0):    
#       print("Average marks in python subject", subsum//len(transpose[i]))    
#     elif(i==1):
#       print("Average marks in Sql subject", subsum//len(transpose[i]))
#     elif(i==2):
#       print("Average marks in Machine Learning subject", subsum//len(transpose[i]))

#use np.where to assisgn pass or fail to each student based on average marks
average_marks=np.mean(marks, axis=1)

# # grades = np.where(average_marks >= 80, "Pass", "Fail")
# # for i in range(len(grades)):
# #     print("Student ", i+1, " has grade: ", grades[i])
# maximum=average_marks[0]
# index=0
# for i in range(len(average_marks)):
#     if(average_marks[i]>maximum):
#         maximum=average_marks[i]
#         index=i
# print("Student ",index+1," has highest performing marks of ",maximum)

std=np.std(transpose)
        
df=pd.DataFrame({
    'total_marks': marks.sum(axis=1),
    'average_marks': average_marks,
    'std_deviation': std,
    'grade': np.where(average_marks >= 80, "Pass", "Fail"),
    'maximum_marks': marks.max(axis=1),
    'minimum_marks': marks.min(axis=1)
    
})   
print(df)            