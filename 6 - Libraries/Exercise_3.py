import pandas as pd

data = {
    "Name": ["Ama", "Kwame", "Akosua", "Yaw", "Esi"],
    "Math": [85, 78, 92, 88, 80],
    "English": [90, 82, 75, 85, 88],
    "Science": [88, 79, 91, 84, 86]
}
df = pd.DataFrame(data)

# Average score per student
df["Average"] = df[["Math", "English", "Science"]].mean(axis=1)
print("Average score per student:\n", df[["Name", "Average"]])

# Students scoring above 80 in all subjects
above_80 = df[(df["Math"] > 80) & (df["English"] > 80) & (df["Science"] > 80)]
print("\nStudents scoring above 80 in all subjects:\n", above_80[["Name", 
    "Math", "English", "Science"]])

# Highest scorer in Math
max_math = df.loc[df["Math"].idxmax()]
print(f"\nHighest scorer in Math: {max_math['Name']} ({max_math['Math']})")