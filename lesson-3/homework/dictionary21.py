dict21 = {'a': 3, 'b': 1, 'c': 2}
sorted_by_value = dict(sorted(dict21.items(), key=lambda item: item[1]))
print("Sorted by Value:", sorted_by_value)