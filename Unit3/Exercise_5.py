# Open the file and read its content
with open("note.txt", "r") as file:
    content = file.read()

# Count words, lines, and characters
words = content.split()
lines = content.splitlines()
characters = len(content)

# Display counts
print("\nWord Count in File:")
print("Words:", len(words))
print("Lines:", len(lines))
print("Characters:", characters)