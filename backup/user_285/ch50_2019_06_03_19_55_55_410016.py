def numero_no_indice(lista):
    lista1 = []
    for i in lista:
        if lista[i]==i:
            lista1.append(i)
    return lista1