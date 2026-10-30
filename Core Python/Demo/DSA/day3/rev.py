li = [18, 7, 23, 88, 89]
left = 0
right = len(li)-1

while left<=right:
    li[left], li[right] = li[right], li[left]
    left+=1
    right-=1
print("List after reversing = ", li)