#  4. Write a program to input all sides of a triangle and check whether triangle is valid or not.
side1 = int(input("Enter side 1 of a triangle: "))
side2 = int(input("Enter side 2 of a triangle: "))
side3 = int(input("Enter side 3 of a triangle: "))

if(side1+side2 >side3 and side1 + side3 > side2 and side2+side3 > side1):
    print("This is a valid traingle.")
else:
    print("This is an invalid triangle.")