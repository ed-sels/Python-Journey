#Accept input
score = float(input("Enter your mark: "))

#Interpretation of score
if score <= 100 and score >= 0:
    if score >= 80:
        grade = "A"

    elif score >= 70:
        grade = "B"

    elif score >= 60:
        grade = "C"

    elif score >= 50:
        grade = "D"

    else:
        grade = "F"

else:
    print("Please input a valid score: ")

# Displaying grade
print("Your grade is", grade)