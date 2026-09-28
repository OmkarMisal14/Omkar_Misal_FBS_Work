# Convert the time entered in hh,min and sec into seconds.
hr = int (input("Enter Hour: "))
min = int(input("Enter Minutes:"))
sec = int(input("Enter second: "))
hr = hr*(60**2)
min = min*60
sec = sec + min + hr
print("Total hr are ",hr)
print("Total min are ",min)
print("Total Seconds are ",sec)