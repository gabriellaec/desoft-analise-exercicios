def fatorial (n):
    fat=1
    if n==0:
        fat=1
        return fat
    else:
        while n>0:
            fat*=n
            n-=1
        return fat

        