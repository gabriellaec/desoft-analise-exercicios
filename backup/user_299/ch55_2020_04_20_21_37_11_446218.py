def encontra_maximo(matriz):
    lista = matriz[0]+matriz[1]+matriz[2]
    maxdalista = 0
    for e in lista:
        if (e**2)**(1/2)>(maxdalista**2)**(1/2):
            maxdalista = e
    modmaxdalista = (maxdalista**2)**(1/2)
        
    return modmaxdalista