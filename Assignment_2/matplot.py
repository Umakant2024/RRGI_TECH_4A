import matplotlib
matplotlib.use("Agg")

from pathlib import Path

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataset_path = Path(__file__).with_name("EducationDataset_2023-24.csv")
df = pd.read_csv(dataset_path)

df.info()
print(df.head())


# Q1: Find the district with the highest and lowest number of schools.

highest = df["No of Schools - Total"].max()
lowest = df["No of Schools - Total"].min()

print("Highest schools:", highest)
print("Lowest schools:", lowest)

print("District with highest schools:",
      df[df["No of Schools - Total"] == highest]["District"].values)

print("District with lowest schools:",
      df[df["No of Schools - Total"] == lowest]["District"].values)


# Q2: Find the district with the highest total student enrollment.

highest_students = df["No of Students - Total"].max()

print("Highest students:", highest_students)

print("District:",
      df[df["No of Students - Total"] == highest_students]["District"].values)


# Q3: Find the district with the largest difference between boys and girls.

difference = np.abs(
    df["No of Students - Boys"] -
    df["No of Students - Girls"]
)

highest_difference = difference.max()

print("Largest gender difference:", highest_difference)

print("District:",
      df[difference == highest_difference]["District"].values)


# Q4: Find the district with the highest Class X pass percentage.

class10 = " PASS PERCENTAGE IN CLASS X - \n(Before Compt.) - 2023-24"

highest_class10 = df[class10].max()

print("Highest Class X:", highest_class10)

print("District:",
      df[df[class10] == highest_class10]["District"].values)


# Q5: Find the district with the highest Class XII pass percentage.

class12 = "PASS PERCENTAGE IN CLASS XII - (Before Compt.) - 2023-24"

highest_class12 = df[class12].max()

print("Highest Class XII:", highest_class12)

print("District:",
      df[df[class12] == highest_class12]["District"].values)


# Q6: Compare Class X and Class XII pass percentages using a line graph.

df["Students Per School"] = (
    df["No of Students - Total"] /
    df["No of Schools - Total"]
)

highest_ratio = df["Students Per School"].max()

print("Highest students per school:", highest_ratio)

print(
    "District:",
    df[df["Students Per School"] == highest_ratio]["District"].values
)


# Q7: Find the relationship between number of schools and Class X pass percentage.

correlation1 = np.corrcoef(
    df["No of Schools - Total"],
    df[class10]
)

print("Schools and Class X Correlation:")
print(correlation1)


# Q8: Find the relationship between total students and Class X pass percentage.

correlation2 = np.corrcoef(
    df["No of Students - Total"],
    df[class10]
)

print("Students and Class X Correlation:")
print(correlation2)


# Q9: Calculate students per school and find its relationship with Class X pass percentage.

correlation3 = np.corrcoef(
    df["Students Per School"],
    df[class10]
)

print("Students Per School and Class X Correlation:")
print(correlation3)


# Q10: Display the highest student enrollment, highest Class X pass percentage, and highest students per school.

print("Highest students:", highest_students)
print("Highest Class X:", highest_class10)
print("Highest students per school:", highest_ratio)


fig, ax = plt.subplots(3, 2, figsize=(16, 12))


ax[0, 0].plot(
    df["District"],
    df["No of Students - Boys"],
    label="Boys"
)

ax[0, 0].plot(
    df["District"],
    df["No of Students - Girls"],
    label="Girls"
)

ax[0, 0].set_title("Boys vs Girls")
ax[0, 0].set_xlabel("District")
ax[0, 0].set_ylabel("Students")
ax[0, 0].tick_params(axis="x", rotation=45)
ax[0, 0].legend()
ax[0, 0].grid(True)


ax[0, 1].plot(
    df["District"],
    df[class10],
    label="Class X"
)

ax[0, 1].plot(
    df["District"],
    df[class12],
    label="Class XII"
)

ax[0, 1].set_title("Class X vs Class XII")
ax[0, 1].set_xlabel("District")
ax[0, 1].set_ylabel("Pass Percentage")
ax[0, 1].tick_params(axis="x", rotation=45)
ax[0, 1].legend()
ax[0, 1].grid(True)


ax[1, 0].scatter(
    df["No of Schools - Total"],
    df[class10]
)

ax[1, 0].set_title("Schools vs Class X")
ax[1, 0].set_xlabel("Number of Schools")
ax[1, 0].set_ylabel("Class X Pass Percentage")
ax[1, 0].grid(True)


ax[1, 1].scatter(
    df["No of Students - Total"],
    df[class10]
)

ax[1, 1].set_title("Students vs Class X")
ax[1, 1].set_xlabel("Total Students")
ax[1, 1].set_ylabel("Class X Pass Percentage")
ax[1, 1].grid(True)


ax[2, 0].bar(
    df["District"],
    df["Students Per School"],
    color="skyblue",
    width=0.6
)

ax[2, 0].set_title("Students Per School")
ax[2, 0].set_xlabel("District")
ax[2, 0].set_ylabel("Students Per School")
ax[2, 0].tick_params(axis="x", rotation=45)
ax[2, 0].grid(True)


ax[2, 1].axis("off")


plt.tight_layout()

plt.savefig("all_graphs.png")

plt.close(fig)