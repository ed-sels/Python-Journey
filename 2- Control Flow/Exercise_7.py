# Importing module math_utils
import math_utlis

# Accepting input
n = int(input("Enter a number greater than 0:"))

# Printing results
print("Factorial of", n, "=",math_utlis.factorial(n))

if math_utlis.is_prime(n) == False:
    print(n, "is not a prime number.")

else:
    print(n, "is a prime number.")