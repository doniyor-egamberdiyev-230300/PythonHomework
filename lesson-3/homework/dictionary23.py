dict23a = {'a': 1, 'b': 2}
dict23b = {'b': 3, 'c': 4}
common_keys23 = set(dict23a.keys()) & set(dict23b.keys())
common_keys = set(dict23a.keys()) & set(dict23b.keys())
print("Common Keys:", common_keys)
