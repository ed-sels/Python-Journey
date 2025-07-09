# Accept user input to enter 3 students' names and GPAs
students = []
for i in range(3):
    name = input(f"Enter student {i+1}'s name: ")
    gpa = float(input(f"Enter student {i+1}'s GPA: "))
    students.append((name, gpa))

# Write information to a file
with open("students.txt", "w") as file:
    for student in students:
        file.write(f"{student[0]} {student[1]}\n")

# Read the file and count students with GPA ≥ 3.0
high_gpa_students = []
with open("students.txt", "r") as file:
    for line in file:
        name, gpa = line.split()
        gpa = float(gpa)
        if gpa >= 3.0:
            high_gpa_students.append(name)

# Print names of students with GPA ≥ 3.0
print("\nStudents with GPA ≥ 3.0:")
for student in high_gpa_students:
    print(student)