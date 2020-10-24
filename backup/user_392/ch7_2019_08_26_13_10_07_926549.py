def calcula_norma(x):
    i=0
    n=0
    while i<len(x):
        n=x[i]**2+n
        i+=1
    return n**(1/2) 