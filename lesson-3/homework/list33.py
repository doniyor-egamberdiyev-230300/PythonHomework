def find_all_indices(lst, element):
    indices = []
    for i, val in enumerate(lst):
        if val == element:
            indices.append(i)
    return indices

print(find_all_indices([1, 2, 3, 2, 4, 2, 5], 2))
