def arcotangente(x,n):
    i=1
    formula=0
    a=1
    while i<=n:
        formula+=a*(x**i)/i
        i+=2
        a=-a
    return formula
    
    