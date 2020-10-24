def numero_no_indice(lista):
    lista1 = []
    for i in range(len(lista)):
        if lista[i]==i:
            lista1.append(i)
    return lista1
