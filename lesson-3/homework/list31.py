def repeat_elements(lst, n):
    return [element for element in lst for _ in range(n)]

# Example
my_list = [1, 2, 3]
print(repeat_elements(my_list, 3))
