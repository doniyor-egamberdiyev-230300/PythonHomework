a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

if len({a, b, c}) == 3:
    print("All numbers are different.")
else:
    print("Some numbers are the same.")
