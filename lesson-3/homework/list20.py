my_list = [10, 20, 30, 40, 50, 40]

unique_list = list(set(my_list))
unique_list.sort()

second_largest = unique_list[-2]

print(second_largest)
