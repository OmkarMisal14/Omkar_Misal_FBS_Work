di = {"Sachin":45,
      "Rohit":96,
      "Virat":88}

print(di)

# Traversing
for i, j in di.items():
    print(i, j)

di["Hardik"] = 67
print(di)
di["Virat"] = 89
print(di) 
print(di["Hardik"])