import random


# MAX_TRIES = 6
# HANGMAN_ASCII_ART = """Welcome to the game Hangman\n
#   _    _
#  | |  | |
#  | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __
#  |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_
#  | |  | | (_| | | | | (_| | | | | | | (_| | | | |
#  |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
#                       __/ |
#                      |___/"""
# print(HANGMAN_ASCII_ART)
# num_of_try = random.randint(5,10)
# print(num_of_try)
#
# print(" 1: "
#       "x-------x")
# print(""" 2:
#     x-------x
#     |
#     |
#     |
#     |
#     |
# """)
# print(""" 3:
#     x-------x
#     |       |
#     |       0
#     |
#     |
#     |
# """)
# print(""" 4:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |
#     |
# """)
# print(""" 5:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |      /|\\
#     |
# """)
# print(""" 6:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |      /|\\
#     |      /
# """)
# print(""" 7:
#     x-------x
#     |       |
#     |       0
#     |       |
#     |      /|\\
#     |      / \\
# """)
#
# char_guess = input("Please enter charter\n").lower()
# print(char_guess)

# word_to_guess = input("Please enter a word: ")
# print("_ " * word_to_guess.__len__())



def check_valid_input(letter_guessed, old_letters_guessed):
      if (letter_guessed.isalpha()) \
            and (len(letter_guessed) == 1) \
            and (letter_guessed not in old_letters_guessed):
        return True
      else:
        return False

def try_update_letter_guessed(letter_guessed, old_letters_guessed):
        letter_guessed = letter_guessed.lower()
        if check_valid_input(letter_guessed, old_letters_guessed):
            old_letters_guessed.append(letter_guessed)
            old_letters_guessed = sorted(old_letters_guessed)
            return True
        else:
            print("X")
            print(" -> ".join(old_letters_guessed))
            return False


old_letters = ['a', 'b', 'c']
try_update_letter_guessed("B", old_letters)
# user_letter_guessed = input("Please enter charter\n").lower()
# print(check_valid_input(user_letter_guessed, old_letters))


