def seven_boom(end_number):
    boom_list = []
    for num in range(0,end_number + 1):
        if num % 7 == 0:
            boom_list.append("BOOM")
        else:
            boom_list.append(num)
    return boom_list



print(seven_boom(30))