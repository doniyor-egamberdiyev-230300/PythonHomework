enter = input("Enter the string you want to acronym: ")
words = enter.split()
acronym = "".join(word[0].upper() for word in words)
print("Acronym:", acronym)