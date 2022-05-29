def extend_list_x(list_x, list_y):
    # list_y.insert(len(list_y),list_x)
    # print (list_y)
    print(list_x[:0])
    list_x[:0] = list_y
    print(list_x)
x = [4, 5, 6]
y = [1, 2, 3]
print((extend_list_x(x,y)))