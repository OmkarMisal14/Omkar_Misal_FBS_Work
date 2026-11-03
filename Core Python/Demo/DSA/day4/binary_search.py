li =[18, 25,36, 47, 58, 69,80]
def binarySearch(li):
    start = 0
    end = len(li)-1
    tar = int(input("Enter num to search: "))
    while start<=end:
        mid = (start+end)//2
        if tar == li[mid]:
            return mid
        elif tar>li[mid]:
            start=mid+1
        else:
            end = mid-1
    else:
        return -1

res = binarySearch(li)
print("Num is found") if res!=-1 else print("Num is not found.")