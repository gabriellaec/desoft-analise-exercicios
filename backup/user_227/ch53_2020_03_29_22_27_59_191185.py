def soma_impares(lista):
    i = 0
    impares = []
    while i < len(lista):
        if lista[i] % 2 != 0:
            impares.append(lista[i])
        
        i += 1
    
    return sum(impares)