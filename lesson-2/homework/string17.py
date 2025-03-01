asked = input("Enter a sentence: ")

vowels = "aeiouAEIOU"

for char in vowels:
    asked = asked.replace(char, "*")

print("Sentence with vowels replaced:", asked)