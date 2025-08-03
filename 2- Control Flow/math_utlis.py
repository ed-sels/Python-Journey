# Declaring function for factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Declaring function for prime number check
def is_prime(n):
    if n <= 1:
        return False
    
    for i in range(2, int(n ** 0.5) +1):
        if n % i == 0:
            return False
        
    return True
