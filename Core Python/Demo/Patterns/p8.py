for i in range(5, 0,-1):
    for j in range(i, 0, -1):
        if i ==5 or j ==1 or j==i:
            print("*", end=' ')
        else:
            print(" ", end=' ')
    print()