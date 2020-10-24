def encontra_maximo(matriz):
    lista = matriz[0]+matriz[1]+matriz[2]
    maxdalista = 0
    for e in lista:
        if e>maxdalista:
            maxdalista = e
        
    return maxdalista