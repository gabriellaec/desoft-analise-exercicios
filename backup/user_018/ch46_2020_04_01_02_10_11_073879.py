def numero_no_indice(lista,n):
    i = 0
    while i < len(lista):
        if n != lista[i]:
            lista.del(i)
        i+=1
    return lista
