def soma_impares(lista):
    i = 0
    k = 0
    while i < len(lista):
        if lista[i] % 2 == 1:
            k = k + lista[i]
        i+=1
    return k