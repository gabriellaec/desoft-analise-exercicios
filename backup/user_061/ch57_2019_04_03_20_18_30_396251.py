def soma_impares(lista):
    lista_impares = []
    i = 0
    while i<len(lista):
        if lista[i] % 2 != 0:
            lista_impares.append(lista)
        i+=1
    return sum(lista_impares)