string = input('Enter a string: ')
string1 = string.lower()
a = 0
b = 0
for char in string1:
 if char.isalpha():
    if char in 'aeiou':
        a += 1
    else:
        b += 1


print(f"The number of vowels: {a}")
print(f"The number of consonants: {b}")

