def calcula_norma(v):
    norma = 0
    for i in v: 
        norma += i**2
    print(norma**(1/2))