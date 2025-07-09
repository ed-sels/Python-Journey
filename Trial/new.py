#Grade assignment
def markGrader(mark):
    
    if mark <= 100 and mark >= 0:
        if mark >= 90:
            grade = 'A'

        elif mark >= 80:
            grade = 'B'

        elif mark >= 70:
            grade = 'C'

        elif mark >= 60:
            grade = 'D'

        else:
            grade = 'F'

    else:
        mark = int(input("Please enter a mark out of 100:"))

    print("Your mark is", mark, "and grade is", grade, ".")

#Check for odd or even
def evenChecker(mark):
    if mark % 2 == 0:
        print("Your mark is even.")

    else:
        print("Your mark is odd.")

#Conversion to float
def floatPrint(mark):
    print("Mark:", mark)
    float_mark = float(mark)
    print("Float Mark:", float_mark)

mark = int(input("Enter your mark out of 100:"))
markGrader(mark)
evenChecker(mark)
floatPrint(mark)