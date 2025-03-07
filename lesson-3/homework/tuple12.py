def second_largest(tpl):
    unique = list(set(tpl))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

print("Second largest:", second_largest((1, 2, 3, 4, 5)))