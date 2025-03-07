def remove_element(tpl, element):
    lst = list(tpl)
    if element in lst:
        lst.remove(element)
    return tuple(lst)

print("Tuple after removal:", remove_element((1, 2, 3, 4, 5), 3))