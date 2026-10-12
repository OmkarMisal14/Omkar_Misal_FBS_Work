# 4. Calculate the cost of painting the following building’s walls (both interior and
# exterior). You need to accept area (one wall) and cost of both interior and
# exterior wall.
# (Note: 1. Below diagram is of two joint rooms.
# 2. It is upper view of building.)
len = float(input("Enter the length: "))
wid = float(input("Enter the width: "))
cost=300
area = len*wid
total_cost = (area*cost)*2
print("Total cost is", total_cost)
