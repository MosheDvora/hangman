def numbers_letters_count(my_str):
    num_of_mumeric, num_of_digit =  0, 0
    for digit in my_str:
        if digit.isnumeric():
            num_of_mumeric += 1
        else:
            num_of_digit += 1
    return [num_of_mumeric, num_of_digit]

print(numbers_letters_count("  abcasdf12#$!3"))