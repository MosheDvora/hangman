def are_lists_equal(list1, list2):
    sort_list1, sort_list2 = sort_lists(list1,list2)
    print(check_if_lists_equal(sort_list1,sort_list2))



def sort_lists(list1,list2):
    list1.sort()
    list2.sort()

    return list1,list2

def check_if_lists_equal(list1,list2):
    if list1 == list2:
        return True
    else:
        return False






list1 = [0.6, 1, 2, 3]
list2 = [3, 2, 0.6, 1]
are_lists_equal(list1,list2)