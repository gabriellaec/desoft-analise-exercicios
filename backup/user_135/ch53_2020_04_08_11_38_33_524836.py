def soma_impares(lista):
    indice = 0
    x = 0
    while indice < int(len(lista)):
        if lista[indice]%2 == 0:
            indice +=1
        else:
            x += lista[indice]
            indice += 1
        return x
            