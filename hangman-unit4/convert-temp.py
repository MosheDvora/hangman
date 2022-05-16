user_temp = input("Insert the temperature you would like to convert:\n")
print(user_temp[0:-1])
if (user_temp[-1].casefold() == "f"):
    print(str((5 * float(user_temp[0:-1])-160) / 9) + "C")


