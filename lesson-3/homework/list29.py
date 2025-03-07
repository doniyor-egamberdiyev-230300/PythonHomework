def remove_by_index(lst, index):
    if 0 <= index < len(lst):  # Ensure the index is valid
        del lst[index]

# Example
my_list = [10, 20, 30, 40, 50]
remove_by_index(my_list, 2)  # Removes the element at index 2 (30)
print(my_list) 
