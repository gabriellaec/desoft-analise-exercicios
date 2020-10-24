def numero_no_indice2 (lista):
    lista_final = []
    for i in range(len(lista)):
        if lista[i] == i:
            lista_final.append(i)
    return lista_final