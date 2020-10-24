def numero_no_indice(lista1):
    i=0
    while i < len(lista1):
        while i != lista1[i]:
            del lista1[i]
        i+=1
    return lista 1
        