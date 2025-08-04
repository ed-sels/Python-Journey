def reverse_word(word):
    if len(word) <= 1:
        return word
    return reverse_word(word[1:]) + word[0]

word = "hello"
print("Word:", word)
print("Reversed word:", reverse_word(word))