def min_in_sublist(lst, start, end):
    return min(lst[start:end])  # Slices the list and finds the minimum
my_list = [3, 7, 2, 9, 5, 8, 4]
print(min_in_sublist(my_list, 1, 5))
