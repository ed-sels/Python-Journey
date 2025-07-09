def is_prime(num):
    """Check if a number is prime."""
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def print_fibonacci(n):
    """Print the Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def main_menu():
    """Display the main menu and handle user input."""
    while True:
        print("\nMenu:")
        print("1. Prime Number Test.")
        print("2. Print Fibonacci sequence.")
        print("3. Exit.")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            num = int(input("Enter a number: "))
            if is_prime(num):
                print(f"{num} is a prime number.")
            else:
                print(f"{num} is not a prime number.")
        elif choice == "2":
            n = int(input("Enter the number of terms: "))
            print_fibonacci(n)
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()