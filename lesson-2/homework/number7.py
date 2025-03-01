number = int(input("Enter a number: "))

num = str(number)[-1]

if num in "24680" and number !=0:
    print(f"The {number} is even")
elif number == 0:
    print(f"The {number} is zero")

else:
    print(f"The {number} is odd")
#
