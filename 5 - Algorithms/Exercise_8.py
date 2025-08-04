def count_vowels(s):
    vowels = "aeiouAEIOU"
    if not s:
        return 0
    return (1 if s[0] in vowels else 0) + count_vowels(s[1:])

word = "recursion"
print(f"Number of vowels in '{word}':", count_vowels(word))