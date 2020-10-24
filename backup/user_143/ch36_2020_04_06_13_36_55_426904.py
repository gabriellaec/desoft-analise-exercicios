def fatorial (n):
    fat=1
    if n==0:
        fat=1
        return fat
    else:
        for e in range (1, n-1):
            fat*=n
            n-=1
        return fat

        