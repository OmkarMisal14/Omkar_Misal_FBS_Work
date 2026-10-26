for i in range(1, 6):
    for k in range(1, 6-i):
        print(" ", end=' ')

    for j in range(i, 2*i):
        print(j, end=' ')
    nm = 2
    for n in range(2*i-2,i-1,-1):
        print(n, end=' ')
    nm+=2
    print()