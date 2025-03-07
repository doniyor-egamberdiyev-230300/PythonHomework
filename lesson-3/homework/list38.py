def is_palindrome(lst):
    return lst == lst[::-1]

print("Is palindrome (True/False):", is_palindrome([1, 2, 3, 2, 1]))  # True
print("Is palindrome (True/False):", is_palindrome([1, 2, 3, 4, 5]))  # False
