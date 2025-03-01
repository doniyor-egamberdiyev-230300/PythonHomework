# Get user input
num = input("Enter a number: ")

# Remove non-digit characters (like '.' or '-')
cleaned_num = num.replace(".", "").lstrip("-")

# Get the last digit
if cleaned_num.isdigit():
    last_digit = cleaned_num[-1]
    print(f"The last digit of {num} is: {last_digit}")
else:
    print("Invalid input. Please enter a valid number.")
