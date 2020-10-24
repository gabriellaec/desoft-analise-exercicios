def soma_impares(lista):
    impares = []
    i = 0
    while i < len(lista):
        if lista[i] % 2 == 0:
            impares.append(lista[i])
        i +=1
    return impares