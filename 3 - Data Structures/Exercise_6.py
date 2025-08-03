# Accept user input to enter 5 favorite colors
colors = []
for i in range(5):
    color = input(f"Enter color {i+1}: ")
    colors.append(color)

# Save the list to a file
with open("colors.txt", "w") as file:
    for color in colors:
        file.write(color + "\n")

# Read the file and print each color in uppercase
with open("colors.txt", "r") as file:
    print("\nColors in Uppercase:")
    for line in file:
        print(line.strip().upper())