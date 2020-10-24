def fatorial(n):
    fat=1
    for i in range(0,n,2):
        fat=fat*(fat-1)
        print(fat)
    return fat