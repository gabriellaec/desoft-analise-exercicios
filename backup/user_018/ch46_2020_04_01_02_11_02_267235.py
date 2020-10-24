def numero_no_indice(lista,n):
    i = 0
    while i < len(lista):
        if n != lista[i]:
            del lista[i]
        i+=1
    return lista
