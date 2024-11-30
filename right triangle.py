""" Author:Joseph francis
    Date 30-11-2024
"""

def is_right_triangle():
    sides=[side1,side2,side3]
    sides.sort()
    if sides[2]**2==sides[0]**2+sides[1]**2:
        return True
    return False


side1=int(input("enter the side 1:"))
side2=int(input("enter the side 2:"))
side3=int(input("enter ths side 3:"))

if is_right_triangle():
    print("The given sides are part of a right triangle")
else:
    print("The given sides are not part of a right triangle")
is_right_triangle()
