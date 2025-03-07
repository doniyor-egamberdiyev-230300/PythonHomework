def is_tuple_sorted(tpl):
    return tpl == tuple(sorted(tpl))

print("Is tuple sorted:", is_tuple_sorted((1, 2, 3)))