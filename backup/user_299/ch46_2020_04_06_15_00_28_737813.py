def numero_no_indice(lista):
    for i,e in enumerate(lista):
        if i!=e:
            del lista[i]
    return lista