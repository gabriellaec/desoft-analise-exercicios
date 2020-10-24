def numero_no_indice(lista):
    lista_numero_indice= []
    i= 0
    while i < len(lista):
        if lista[i]== i:
            lista_numero_indice.append(i)
            i= i + 1
    return lista_numero_indice