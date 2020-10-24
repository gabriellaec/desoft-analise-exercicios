def calcula_norma(lista):
    v=0
    i=0
    while i<len(lista):
        v+= lista[i]**2
        i+=1
    return v**(1/2)
        