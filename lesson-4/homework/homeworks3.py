def insert_underscores(txt):
    result = []
    vowels = "aeiouAEIOU"
    count = 0  # Harflarni hisoblash

    for i in range(len(txt)):
        result.append(txt[i])
        count += 1

        # Har 3 ta harfdan keyin underscore qo'yish
        if count % 3 == 0 and txt[i] not in vowels:
            if i + 1 < len(txt) and txt[i + 1] != '_':
                result.append('_')

    return ''.join(result)


# Test cases
print(insert_underscores("hello"))  # hel_lo
print(insert_underscores("assalom"))  # ass_alom
