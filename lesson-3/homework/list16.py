my_list = [2, 4, 3,5, 7, 0, 1]
odd = 0

for num in my_list:
    if  num  % 2 != 0:  # if when we divided 2 then reminder is not equal to 0. it is even number
        odd += 1

print(odd)