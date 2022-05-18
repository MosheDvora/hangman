def format_list(my_list):
    new_list = ",".join(my_list[:-1:2])
    new_list = new_list + " and " + my_list[-1]
    return new_list


my_list = ["hydrogen", "helium", "lithium", "beryllium", "boron", "magnesium", "aaa", "bbb"]
print(format_list(my_list))