def soma_impares(lista):
    i = 0
    S = 0
    while i < len(lista):
        if lista[i] % 2 != 0:
            S += lista[i]
            
        i += 1
        return S