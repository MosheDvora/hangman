def chocolate_maker(small, big, x):
    mod_x_5 = x % 5
    div_x_5 = x // 5

    if x >= 5:
        if big >= div_x_5:
            if mod_x_5 == 0:
                result = True
            elif small >= mod_x_5:
                result = True
            else:
                result = False
        elif small >= (x - 5 * big):
            result = True
        else:
            result = False
    else:
        if small >= x:
            result = True
        else:
            result = False

    print(result)


chocolate_maker(9,0,15)