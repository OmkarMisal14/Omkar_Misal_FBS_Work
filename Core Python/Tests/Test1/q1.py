# 1. Write a program to find the area and perimeter of following figure (Accept the length, breadth and radius from user:
len = float(input("Enter length: "))
wid = float(input("Enter width: "))
rad = float(input("Enter rad: "))

rect = len*wid
circle = (22/7)*rad**2
circle/=2
total_area = rect+circle
print("Total area is", total_area)
