def arcotangente(x,n):
    i=1
    formula=0
    while i<=n:
        formula+=(1/i)*(x**i)
        i+=2
        i=-i
    return formula
    