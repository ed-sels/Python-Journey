import pandas as pd

# Read CSV file
df = pd.read_csv('students.csv')

# Students in Level 300
level_300 = df[df['Level'] == 300]
print("Students in Level 300:\n", level_300)

# Average GPA of all students
avg_gpa = df['GPA'].mean()
print("\nAverage GPA of all students:", avg_gpa)

# Students with GPA less than 2.5
low_gpa = df[df['GPA'] < 2.5]
print("\nStudents with GPA less than 2.5:\n", low_gpa)