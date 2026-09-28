# Convert distant given in feet and inches into meter and centimeter.
feet = int (input("Enter Feet:"))
Inch = int (input("Enter Inch: "))
f_cm = feet*30

I_cm = Inch*2.5
print(f"Meter is {f_cm} and centimeter is {I_cm}")

T_centi = f_cm + I_cm
meter = T_centi//100
Final_centi =  T_centi%100
print(f"Meter is {meter} and centimeter is {Final_centi}")