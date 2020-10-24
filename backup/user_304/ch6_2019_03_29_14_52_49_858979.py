def encontra_maximo (lista):
    i=0
    maior=lista[0][0]
    while i<len(lista):
        j=0
        while j<len(lista[i]):
            if lista[i][j]>maior:
                maior=lista[i][j]
            j+=1
        i+=1
    return maior 
        