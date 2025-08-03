# Accepting number
num = int(input("Enter a number:"))
final_num = 0

# Using the loop to reverse the number
while num > 0:
    value = num % 10
    final_num = final_num * 10 + value
    num = num// 10

print(final_num)