def fatorial(n):
    fat=0
    for i in range(0,n,2):
        fat=fat*(fat-1)
    return fat