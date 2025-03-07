def second_smallest(tpl):
    unique = list(set(tpl))
    unique.sort()
    return unique[1] if len(unique) >= 2 else None

print("Second smallest:", second_smallest((1, 2, 3, 4, 5)))