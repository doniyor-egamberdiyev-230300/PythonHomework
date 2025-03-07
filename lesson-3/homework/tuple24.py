def is_palindrome(tpl):
    return tpl == tpl[::-1]

print("Is palindrome:", is_palindrome((1, 2, 3, 2, 1)))
