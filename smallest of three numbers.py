'''Author:Joseph Francis
   Date:15-10-2024
   program to determine the smallest of three numbers
'''

n1=int(input("enter a number:"))
n2=int(input("enter a number:"))
n3=int(input("enter a number:"))
if n1<n2 and n1<n3:
    print(n1,"is the smallest value")
elif n2<n1 and n2<n3:
    print(n2,"is the smallest value")
else:
    print(n3,"is the smallest value")