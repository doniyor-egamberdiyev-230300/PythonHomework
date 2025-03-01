words = input("Enter words separated by spaces: ").split()
char_separate = input("Enter a character to separate words: ")

separated = char_separate.join(words)

print("Here is the joined string", separated)