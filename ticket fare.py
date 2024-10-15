'''Author=Joseph Francis
   Date:15-10-2024
   program to determine the entry ticket fare in a zoo based on age
'''



Age=int(input("enter your age:"))
if Age<10:
    print("fare is 7")
elif Age>=10 and Age<60:
    print("fare is 10")
else:
    print("fare is 5")