def unique_elements(lst):
    seen = set()
    return [x for x in lst if not (x in seen or seen.add(x))]

print("Unique elements in order:", unique_elements([1, 2, 2, 3, 4, 3, 5]))
