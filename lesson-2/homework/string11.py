string = input("Enter a string: ")
chek_digit = any(char.isdigit() for char in string)
count_digit = sum(char.isdigit() for char in string)
if chek_digit:
    print(f"The string contains {count_digit} digits.")

else:
    print("The string does not contains any digit.")