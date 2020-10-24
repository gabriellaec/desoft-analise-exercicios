def estritamente_crescente(lista):
    i = 1
    while i < len(lista):
        if lista[i] <= lista[i-1]:
            del lista[i]
        i += 1
    
    return lista