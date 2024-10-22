'''Author:Joseph Francis
   Date:22/10/2024
   program to convert celsius to fahrenheit and viceversa
'''



temp=int(input("Enter the temperature:"))
a=input("Is this is (C)elsius or (F)ahrenheit?")
if a=='C':
    f=(9/5*temp)+32
    print(temp,"celsius is",f,"fahrenheit")
elif a=="F":
    c=5/9*(temp-32)
    print(temp,"fahrenheit is",c,"celsius")
else:
    print("invalid temperature")
