my_num1 = float(input("Enter the first number: "))
my_num2 = float(input("Enter the second number: "))

if my_num1 + my_num2 > 50.8:
    print(f"Sum of two numbers is greater than 50.8")
elif my_num1 + my_num2 == 50.8:
    print(f"Sum of two numbers is equal to 50.8")
else:
    print(f"Sum of two numbers is less than 50.8")

my_num = float(input("\nEnter a number to check if it's between 10 and 20 (inclusive): "))
if 10 <= my_num  <= 20 :
          print(f"The number {my_num} is between 10 and 20 (inclusive).")
else:
    print(f"The number {my_num} is not between 10 and 20.")
