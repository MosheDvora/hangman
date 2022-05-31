def squared_numbers(start, stop):
    list_sqr = []
    while start <= stop:
        list_sqr.append(start * start)
        start += 1
    return list_sqr

print(squared_numbers(-3,8))