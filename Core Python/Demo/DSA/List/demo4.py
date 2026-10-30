li=[15,33,22,4,56]
large = li[0]
seconl = li[0]
smll = li[0]
for i in range(1, len(li)):
    if li[i]>large:
        large = li[i]
    else:
        if seconl<li[i]:
            seconl = li[i]
            print("THis is second", seconl)


    if li[i]<smll:
        smll = li[i]

print("Largest element is", large)
print("Largest element is", seconl)
print("Largest element is", smll)