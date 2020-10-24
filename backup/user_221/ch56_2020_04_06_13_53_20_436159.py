def calcula_norma(lista):
    norma = abs(lista[0])
    for i in range(len(lista)):     
        if abs(lista[i]) > norma:
            norma = abs(lista[i])
    return norma
            
    