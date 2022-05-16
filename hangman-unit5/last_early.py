def last_early(my_str1):
    if my_str1.casefold()[-1] in my_str1[0:-1]:
        print("ok")
    else:
        print("not ok")


last_early("sdafsdf")