def arcotangente(x, n):
    i=1
    a=0
    
    while -1<x<1:
        if i<=n: 
            a= a + x**i/i
            i += 2
            a= a - x**i/i
            i += 2
        