def calcula_norma(x):
    i=0
    while i<len(x):
        z=x[i]**2+x[i+1]**2
        y=z**(1/2)
        i+=1
    return y 