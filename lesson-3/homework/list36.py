def sum_of_positives(lst):
    return sum(num for num in lst if num > 0)

# Example
my_list = [3, -1, 4, -2, 5, 0]
print(sum_of_positives(my_list))
