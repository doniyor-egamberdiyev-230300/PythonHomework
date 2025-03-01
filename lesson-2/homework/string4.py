string = input("Enter a string: ")
string1= string.lower()

if string1 == string1[::-1]:
    print(f'"{string}" is a palindrome.')
else:
    print(f'"{string}" is not a palindrome.')
