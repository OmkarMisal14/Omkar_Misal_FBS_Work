# 5. Python Program to Find the Union of two Lists without
# using set concept.
L1 = [1, 2, 3, 4, 5]
L2 = [4, 5, 6, 7, 8]

L3 = []

for num in L1:
    if num not in L3:
        L3.append(num)

for num in L2:
    if num not in L3:
        L3.append(num)

print("Union of two lists:", L3)
