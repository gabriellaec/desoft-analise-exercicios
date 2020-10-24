def numero_no_indice(lista):
    i=0
    while i<len(lista):
        if lista[i]!=i:
            del lista[i]
        return lista 