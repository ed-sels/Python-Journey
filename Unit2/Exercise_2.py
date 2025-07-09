# Accepting number
num = int(input("Enter a number:"))

i = 1

# Using loop to create multiplication table
for i in range(1,11):
    print(num , "*", i, "=", num * i)