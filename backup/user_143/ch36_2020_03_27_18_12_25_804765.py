def fatorial (n):
    fat=n
    if n==0:
        fat=1
        return fat
    else:
        while n>0:
            n-=1
            fat*=n
        return fat

        