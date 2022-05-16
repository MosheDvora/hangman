def filter_teens(a=13, b=13, c=13):
    total_age = 0
    if (a >= 13 and a <=19) and (not(a == 15 or a == 16)):
        a = 0
    elif (b >= 13 and b <=19) and (not(b == 15 or b == 16)):
        b = 0
    elif (c >= 13 and c <=19) and (not(c == 15 or c == 16)):
        c = 0
    return a + b + c

print(filter_teens(13,13,1))
