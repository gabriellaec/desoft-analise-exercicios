def numero_no_indice(lista):
    i = 0
    lista_indice = []
    while i < len(lista):
        if lista[i] == i:
           lista_indice.append(i)
        i += 1
    
    return lista_indice