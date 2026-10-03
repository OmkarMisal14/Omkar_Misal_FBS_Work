#  3. Write a program to input angles of a triangle and check whether triangle is valid or not.
angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

total = angle1 + angle2+ angle3
if(total == 180):
    print("This is a valid triangle.")
else:
    print("This is an invalid triangle")