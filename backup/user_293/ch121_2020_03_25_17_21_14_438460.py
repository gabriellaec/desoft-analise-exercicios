def subtracao_de_listas(lista1,lista2):
    i = 0
    while i < len(lista1):
        e = 0
        while e < len(lista2):
            if lista1[i] == lista2[e]:
                del lista1[i]
            e += 1
        i += 1
    return lista1
            
    