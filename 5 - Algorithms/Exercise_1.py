import time

def Recursive_Fibonacci(n):
    if n <= 1:
        return n
    return Recursive_Fibonacci(n-1) + Recursive_Fibonacci(n-2)

def Iterative_Fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

n = 10

start_recursive = time.time() # Recursive performance
result_recursive = Recursive_Fibonacci(n)
end_recursive = time.time()

start_iterative = time.time() # Iterative performance
result_iterative = Iterative_Fibonacci(n)
end_iterative = time.time()

print(f"Recursive Fibonacci({n}): {result_recursive}, Time: {end_recursive - start_recursive:.6f} seconds")
print(f"Iterative Fibonacci({n}): {result_iterative}, Time: {end_iterative - start_iterative:.6f} seconds")