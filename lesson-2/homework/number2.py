num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

largest = max(num1, num2, num3)
smallest = min(num1, num2, num3)

print(f"The largest number is: {largest:>6}")
print(f"The smallest number is: {smallest:>5}")

