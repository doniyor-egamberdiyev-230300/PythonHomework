def sum_of_negatives(lst):
    return sum(num for num in lst if num < 0)

print("Sum of negative numbers:", sum_of_negatives([3, -1, 4, -2, 5, 0]))