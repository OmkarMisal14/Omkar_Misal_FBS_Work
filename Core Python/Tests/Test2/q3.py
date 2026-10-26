# 3. A farmer has a field which is half in circle share and rest rectangle. He needs to do fencing for entire field using barbed wire 5 times. Circular section has radius 20m and rectangle length is 50 m and breadth is 40m. If cost of barbed wire is 35Rs/m then calculate the total cost of fencing the field.

radius = 20
len = 50
width = 40
wire_cost = 35

perimtr = 2*(len+width)
circumference = 2*3.14*radius
total_perimeter = perimtr - width + circumference
wire_len = total_perimeter*5
total_cost = wire_len *35

print("Total cost of fencing the field is", total_cost)