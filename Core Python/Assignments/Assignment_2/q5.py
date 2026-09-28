# WAP to calculate selling price of book based on cost price and discount.
cost_price = float(input("Enter Cost Price: "))
discount = float(input("Enter Discount: "))
selling_price = cost_price-(cost_price*(discount/100))
print(f"Selling Price is {selling_price}")