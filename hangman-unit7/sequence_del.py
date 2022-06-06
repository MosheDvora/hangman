# def sequence_del(my_str):
#     clean_list = []
#     new_list = []
#     for char in my_str:
#         if char not in clean_list:
#                 clean_list.append(char)
#         if char == " ":
#             new_list = new_list + clean_list
#             clean_list = []
#     print("".join(clean_list))
#     print(new_list)
def sequence_del(my_str):
    words, sentence_list = [], ""
    my_list = my_str.split(" ")
    for part_str in my_list:
        for char in part_str:
            if char not in words:
                words.append(char)
        sentence_list = sentence_list + " " + "".join(words)
        words = []
    print(sentence_list[1:])

sequence_del("Heeyyy yyouuuu!!!")