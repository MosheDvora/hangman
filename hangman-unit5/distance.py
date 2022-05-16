def distance(num1, num2, num3):
    if ((abs(num2) - abs(num1)) < 2 or (abs(num3) - abs(num1)) < 2) and \
            ((abs(num2) - abs(num1)) > 1 or (abs(num3) - abs(num1)) > 1):
        return True
    else:
        return False



print(distance(4,5,3)
)