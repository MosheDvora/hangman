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


def is_valid_input(letter_guessed):
      if (not letter_guessed.isalpha()) and (len(letter_guessed) > 1):
            return False
      elif not letter_guessed.isalpha():
            return False
      elif len(letter_guessed) > 1:
            return False
      else:
            return True


user_letter_guessed = input("Please enter charter\n").lower()
print(is_valid_input(user_letter_guessed))

