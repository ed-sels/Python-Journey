# Accepting password
password = input("Enter your password: ")

# Validating password
while password != "Python123":
    print("Wrong password")
    password = input("Enter your password: ")

# Display successful login message
print("Login successful")