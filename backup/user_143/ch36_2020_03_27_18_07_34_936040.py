def fatorial (n):
    s=n
    fat=n
    if n==0:
        fat=1
        return fat
    else:
        while s>0:
            s-=1
            fat*=s
        return fat

        