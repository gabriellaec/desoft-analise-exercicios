def numero_no_indice(lista):
    i = 0
    while i < len(lista):
        if i != lista[i]:
            del lista[i]
        i+=1
    return lista
