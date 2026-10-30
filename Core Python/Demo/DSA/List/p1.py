li=	[2,3,45,56,67]
large = li[0]
second_large = [1]
small = li[0]
second_small = li[1]
for i in range(1, len(li)):
    if li[i]>large:
        second_large = large
        large = li[i]
    else:
        if li[i] > second_large and li[i] != large:
            second_large = li[i]

    if li[i]<small:
        second_small = small
        small = li[i]
    else:
        if li[i]< second_small and li[i] !=large:
            second_small = li[i]
    

print(f"The largest number is {large}")
print(f"Tha second largest number is {second_large}")
print(f"The smallest number is {small}")
print(f"Tha second smallest number is {second_small}")