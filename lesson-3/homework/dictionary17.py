dict17 = {'a': {'x': 100}}
key17 = 'a'
nested_key17 = 'x'
nested_value17 = dict17.get(key17, {}).get(nested_key17)
print("17. Get Nested Value:", nested_value17)