def rotate_list(lst, k):
    k %= len(lst)  # Ensure k doesn't exceed list length
    return lst[-k:] + lst[:-k]

# Example
my_list = [1, 2, 3, 4, 5]
print(rotate_list(my_list, 2))
