def max_in_sublist(lst, start, end):
    if start < 0 or end > len(lst) or start >= end:
        raise ValueError("Invalid range for sublist")
    return max(lst[start:end])

# Example
my_list = [3, 7, 2, 9, 5, 8, 4]
print(max_in_sublist(my_list, 1, 5))  # Sublist [7, 2, 9, 5] → max is 9
