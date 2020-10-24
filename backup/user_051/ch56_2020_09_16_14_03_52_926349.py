def calcula_norma(lista):
    i=0
    a=0
    while i <len(lista):
        a+=lista[i]**2
        i+=1
    return a**(1/2)