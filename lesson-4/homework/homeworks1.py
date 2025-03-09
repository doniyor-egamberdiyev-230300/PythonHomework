from collections import Counter


def find_uncommon_elements(list1, list2):
    count1 = Counter(list1)
    count2 = Counter(list2)
    result = []

    # Add elements from list1 not in list2
    for elem, count in count1.items():
        if elem not in count2:
            result.extend([elem] * count)

    # Add elements from list2 not in list1
    for elem, count in count2.items():
        if elem not in count1:
            result.extend([elem] * count)

    return result


# Test cases
list1 = [1, 1, 2]
list2 = [2, 3, 4]
print(find_uncommon_elements(list1, list2))  # Output: [1, 1, 3, 4]

list1 = [1, 2, 3]
list2 = [4, 5, 6]
print(find_uncommon_elements(list1, list2))  # Output: [1, 2, 3, 4, 5, 6]

list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]
print(find_uncommon_elements(list1, list2))  # Output: [2, 2, 5]