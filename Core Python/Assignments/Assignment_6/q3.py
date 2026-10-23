for i in range(5):
    for g in range(5-i-1):
        print(" ", end=' ')
    num = 1
    for j in range(0, i+1):
        print(num, end='  ')
        num = num*(i-j)//(j+1)


    print()