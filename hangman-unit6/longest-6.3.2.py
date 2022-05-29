def longest(my_list):
    my_list_sorted = sorted(my_list, key=len)
    print(my_list_sorted[-1])


list1 = ["111", "234", "2000", "gorasdfasdfasdu", "birthday", "09"]
longest(list1)
