def fatorial (n):
    s=1
    fat=n
    if n==0:
        fat=1
        return fat
    else:
        while s<n:
            s+=1
            fat*=s
        return fat

        