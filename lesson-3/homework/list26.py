def find_middle_elements(lst):
    n = len(lst)
    mid = n // 2  # Integer division to find the middle index

    if n % 2 == 0:  # Even length: return two middle elements
        return [lst[mid - 1], lst[mid]]
    else:  # Odd length: return the middle element
        return [lst[mid]]


print(find_middle_elements([1, 2, 3, 4, 5]))  # [3] (odd length)
print(find_middle_elements([1, 2, 3, 4, 5, 6]))  # [3, 4] (even length)
