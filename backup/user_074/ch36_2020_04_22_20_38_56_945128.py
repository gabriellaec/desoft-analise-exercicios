def fatorial(n):
    x=0
    print(n)
    while n>x and x!=n:
        nfac=1
        nfac*=(n-x)
        x+=1
    return nfac