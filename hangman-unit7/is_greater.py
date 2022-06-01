def is_greater(my_list, n):
    new_list = []
    for num in my_list:
        if num <= n:
            continue
        new_list.append(num)
    return new_list


def is_greater_new(my_list, n):
    new_list = []
    for num in my_list:
        if num > n:
            new_list.append(num)

    return new_list



print(is_greater([1,2,4,5,6],4))

print((is_greater_new([1,2,4,5,6],4)))