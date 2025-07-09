print("Enter your age:")
age = int(input())

print("Enter your GPA:")
gpa = float(input())

if age >= 18:
    print("Adult:", True)

    if gpa >3.0 and gpa <= 4.0:
        print("High GPA:", True)
        print("Eligible for Honors:", True)

    elif gpa >= 0.0 and gpa <= 3.0:
        print("High GPA:", False)
        print("Eligible for Honors:", False)

    else:
        print("High GPA:", False)
        print("Eligible for Honors:", False)

else:
    print("Adult:", False)
    
    if gpa >3.0 and gpa <= 4.0:
        print("High GPA:", True)
        print("Eligible for Honors:", True)

    elif gpa >= 0.0 and gpa <= 3.0:
        print("High GPA:", False)
        print("Eligible for Honors:", False)

    else:
        print("High GPA:", False)
        print("Eligible for Honors:", False)