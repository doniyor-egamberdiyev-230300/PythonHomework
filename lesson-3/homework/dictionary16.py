dict16 = {'a': {'x': 1}, 'b': 2}
has_nested_dict16 = any(isinstance(v, dict) for v in dict16.values())
print("16. Check for Nested Dictionaries:", has_nested_dict16)