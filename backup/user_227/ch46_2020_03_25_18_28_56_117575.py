def numero_no_indice(lista):
    i = 0
    while i < len(lista):
        if not lista[i] == i:
            del lista[i]
            i += 1
        else:
            i += 1
    
    return lista
