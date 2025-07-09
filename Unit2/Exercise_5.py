import random

# Generate random number from 1 and 50
num = random.randint(1,50)

i = 5

# Validate guess against number
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

# Generate message for a loss
if guess != num and i == 0:
    print("You are out of chances!")
    print("Game Over!")