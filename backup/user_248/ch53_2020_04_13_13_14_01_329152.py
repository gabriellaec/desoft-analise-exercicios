def soma_impares(lista):
    s = 0
    i = 1
    while i < len(lista):
        if lista[i] % 2 !=0: 
            s += lista[i]
        i += 2
    return s
         