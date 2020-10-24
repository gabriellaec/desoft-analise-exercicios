def arcotangente(x,n):
    i=1
    formula=0
    a=1
    while i<=n:
        formula+=a*(1/i)*(x**i)
        i+=2
        a=-a
    return formula
    
    