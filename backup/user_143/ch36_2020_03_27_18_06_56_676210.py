def fatorial (n):
    s=n
    fat=n
    if n==0:
        fat=1
        print (fat)
    else:
        while s>0:
            s-=1
            fat*=s
        print (fat)

        