# Declaration of function
def calculator(a, b, op):

    #Interpretation of operators
    if op == "+" or op == "add":
        calc = a + b
        print("Result:", a, "+", b, "=", calc) 

    elif op == "-" or op == "sub":
        calc = a - b
        print("Result:", a, "-", b, "=", calc)

    elif op == "*" or op == "multiply":
        calc = a * b
        print("Result:", a, "*", b, "=", calc)

    elif op == "/" or op == "divide":
        calc = a / b
        print("Result:", a, "/", b, "=", calc)

    else:
        print("Invalid operator!")

# Accepting values
a = int(input("Enter the first value: "))
b = int(input("Enter the second value: "))
op = input("Enter the operator: ")

# Calling the function
calculator(a, b, op)