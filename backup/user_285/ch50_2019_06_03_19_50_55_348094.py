def numero_no_indice(lista):
    for i in len(lista):
        if lista[i]==i:
            lista.append(i)
    return lista