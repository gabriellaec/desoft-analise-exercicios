def numero_no_indice(lista):
    result = []
    i = 0
    
    while i < len(lista):
        if lista[i] != i:
            result.append(lista[i])
        i = i + 1
    
    return result