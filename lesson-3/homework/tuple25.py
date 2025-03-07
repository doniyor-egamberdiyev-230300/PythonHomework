def unique_elements(tpl):
    seen = set()
    return tuple(x for x in tpl if not (x in seen or seen.add(x)))

print("Unique elements:", unique_elements((1, 2, 2, 3, 4, 3, 5)))