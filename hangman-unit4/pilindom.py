word = input("Enter a word\n")
word = "".join((word.casefold().split()))
rev_word = word[::-1]
if word == rev_word:
    print("pilindom")
else:
    print("not pilindom")