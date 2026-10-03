#  5. Write a program to check whether the triangle is equilateral, isosceles or scalene triangle.
side1 = int (input("Enter side 1 of a triangle: "))
side2 = int (input("Enter side 2 of a triangle: "))
side3 = int (input("Enter side 3 of a triangle: "))

if(side1 == side2 and side2 == side3):
    print("It is equilateral triangle.")
elif(side1== side2 or side2 == side3 or side1 == side3):
    print("It is isosceles triangle")
else:
    print("It is a scalene triangle")