class Course:
    def __init__(self, code, title, credits):
        self.code = code
        self.title = title
        self.credits = credits

    def __str__(self):
        return f"{self.code}: {self.title} ({self.credits} credits)"

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.registered_courses = []

    def register_course(self, course):
        self.registered_courses.append(course)
        print(f"You have registered for: {course}")

    def list_registered_courses(self):
        print(f"{self.name} ({self.student_id}) registered courses:")
        for course in self.registered_courses:
            print(course)

course1 = Course("COMP 106", "Intro to Computer Science", 3)
course2 = Course("MATH 102", "Calculus I", 4)
course3 = Course("COMP 303", "Research Methods", 2)

all_courses = [course1, course2, course3] # Store courses in a list
student = Student("Ruth Ato", "UEB3508022")

print("Available courses:") # Let the student register courses interactively
for item, course in enumerate(all_courses, 1):
    print(f"{item}. {course}")

selected = input("Enter course numbers to register (comma separated): ")
selected_indices = [int(i.strip()) - 1 for i in selected.split(",") 
                    if i.strip().isdigit()]

for item in selected_indices:
    if 0 <= item < len(all_courses):
        student.register_course(all_courses[item])