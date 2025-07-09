numbers = ()

for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    numbers += (num,)

print("\nTuple:", numbers)

# Display maximum and minimum numbers
print("Maximum Number:", max(numbers))
print("Minimum Number:", min(numbers))

# Display frequency of a specific number
specific_number = int(input("\nEnter a number to find its frequency: "))
frequency = numbers.count(specific_number)
print(f"The number {specific_number} appears {frequency} times.")

# Display index of a given number
given_number = int(input("\nEnter a number to find its index: "))
try:
    index = numbers.index(given_number)
    print(f"The index of {given_number} is {index}.")
except ValueError:
    print(f"The number {given_number} does not exist in the tuple.")