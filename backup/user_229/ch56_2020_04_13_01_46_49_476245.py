def calcula_norma(v):
    norma = 0
    for i in range(len(v+1)): 
        norma += i**2
    return norma**(1/2)