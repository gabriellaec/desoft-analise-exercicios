def soma_impares(lista):
    lista=[54, 58, 24]
    s = 0
    i = 1
    while i < len(lista):
        if lista[i] % 2 !=0: 
            s += lista[i]
        i += 1
    return s
         