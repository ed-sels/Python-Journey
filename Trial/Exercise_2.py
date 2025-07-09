import random

#Number Guessing Game
def NumberGuessingGame():
    num = random.randint(1,50)

    i = 5

    while i > 0:

        guess = int(input("Enter a number :"))
        i -= 1

        if guess == num:
            print("You won!")
            break

        elif guess > num:
            print("Too high") 
            print("Tries left:", i )

        else:
                print("Too low")
                print("Tries left:", i )

    if guess != num and i == 0:
        print("You are out of chances!")
        print("Game Over!")

# Multiplication table
def MultiplicationTable():
    num = int(input("Enter a number:"))

    i = 1
    for i in range(1,11):
        print(num + "X Table")
        print(num , "*", i, "=", num * i)

#Area Of Circle
def AreaOfCircle():
    radius = (int(input("Enter your radius: ")))
    unit = input("Enter your unit: ")
    area = 22/7 * radius^2

    print("The area of the circle is", area + unit ,"^2")

#Number Reversal
def NumberReversal():
    num = int(input("Enter a number:"))
    final_num = 0

    while num > 0:
        value = num % 10
        final_num = final_num * 10 + value
        num = num// 10

    print(final_num)


def main():
    while True:
        print("\nMenu:")
        print("1. Number Guessing Game")
        print("2. Multiplication table")
        print("3. Number Reversal")
        print("4. Area Of Circle")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            NumberGuessingGame()
        elif choice == "2":
            MultiplicationTable()
        elif choice == "3":
            NumberReversal()
        elif choice == "4":
            AreaOfCircle()
            break
        elif choice == "5":
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()