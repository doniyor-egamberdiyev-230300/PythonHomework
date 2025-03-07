def check_element(tpl, element):
    return element in tpl

print("Is element present:", check_element((1, 2, 3, 4, 5), 3))