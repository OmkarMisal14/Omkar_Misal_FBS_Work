# 3. Write a program to accept distance in km and convert it into meters and centimeters both.
dist = float(input("Enter the distance: "))
meter = dist*1000
print("Meters:",meter)    
centi = meter*100
print("Centimeter:", centi)