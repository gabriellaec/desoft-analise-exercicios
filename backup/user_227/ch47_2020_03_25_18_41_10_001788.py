def numero_no_indice(lista):
    i = 1
    while i < len(lista):
        if lista[i] <= lista[i-1]:
            del lista[i]
        i += 1
    
    return lista