def numero_no_indice(lista):
    for i in len(lista):
        if lista[i]!=i:
            lista.del(lista[i])
    return lista