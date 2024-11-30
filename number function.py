""" Author:Joseph francis
    date:30th november 2024
"""


def checking_number():
    number1=input("Enter a number:")
    if len(number1)==10 and number1[0]=="9" or number1[0]=="8" or number1[0]=="7":
        print("valid number")
    else:
        print("invalid number")
checking_number()

