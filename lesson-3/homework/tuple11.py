def all_indices(tpl, element):
    return [i for i, val in enumerate(tpl) if val == element]

print("All indices:", all_indices((1, 2, 3, 2, 4, 2, 5), 2))