# for multiple element
tu= (1,2,3,4,5,6)
print(type(tu))
print(tu)

#  for single element 
tp = (2)
print(type(tp))
print(tp)
#  so you need to mention it like tp = (2, )
tp = (2,)
print(type(tp))
print(tp)

# direct traversing
for i in tu:
    print(i)

# Indirect traversing
for i in range(len(tu)):
    print(tu[i])

# reverse indexing
print(tu[-1])

# Slicing
print(tu[::])
print(tu[2:len(tu):])

print(tu[::-1])