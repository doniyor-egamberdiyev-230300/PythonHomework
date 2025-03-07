dict22 = {'a': 10, 'b': 5, 'c': 20}
filtered_dict22 = {k: v for k, v in dict22.items() if v > 10}
filtered_dict = {k: v for k, v in dict22.items() if v > 1}
print("Filtered by Value (value > 1):", filtered_dict)