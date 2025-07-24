def gradeInterpretation(score):
    if score < 0 and score > 100:
        print("Invalid score!")
    elif score < 100:
        print("Score:", score)
        print("Grade: A")
    elif score < 80:
        print("Score:", score)
        print("Grade: B")
    elif score < 70:
        print("Score:", score)
        print("Grade: C")
    elif score < 60:
        print("Score:", score)
        print("Grade: D")
    else:
        print("Score:", score)
        print("Grade: F")

gradeInterpretation(int(input("Please enter your score:")))