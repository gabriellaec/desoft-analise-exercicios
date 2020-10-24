def soma_impares(lista):
    total=0
    for e in range (1,len(lista),2):
        total+=lista[e]
    return total