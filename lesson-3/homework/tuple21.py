def repeat_elements(tpl, n):
    return tuple(element for element in tpl for _ in range(n))

print("Repeated elements:", repeat_elements((1, 2, 3), 2))