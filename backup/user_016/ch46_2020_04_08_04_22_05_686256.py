def numero_no_indice(lista):
    i = 0
    lista_final = []
    while i < len(lista):
        if lista[i] == i:
            lista_final.append(lista[i])
        else:
            pass
    return lista_final