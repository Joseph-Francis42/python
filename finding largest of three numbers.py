'''Author=Joseph Francis
   Date=22/10/2024
   program to determine the largest of three nunmbers
'''



number1=int(input("Enter first number:"))
number2=int(input("Enter second number:"))
number3=int(input("Enter third number:"))
if number1>number2 and number1>number3:
    print("The largest number is:",number1)
elif number2>number1 and number2>number3:
    print("The largest number is:",number2)
else:
    print("The largest number is:",number3)
