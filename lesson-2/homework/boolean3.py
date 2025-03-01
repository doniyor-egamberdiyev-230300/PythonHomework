num = float(input("Enter a number: "))

if num > 0 and num.is_integer() and int(num) % 2 == 0:
    print(f"{int(num)} is a positive even number.")
elif num > 0:
    print(f"{int(num)} is positive but not even.")
else:
    print(f"{int(num)} is not a positive even number.")