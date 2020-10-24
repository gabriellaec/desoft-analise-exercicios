def calcula_norma(lista):
    norma = lista[0][0]
    for i in range(len(lista)):
        for j in range(len(lista[i])):
            if abs(lista[i][j]) > norma:
                norma = abs(lista[i][j])
    return norma
            
    