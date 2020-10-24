def subtracao_de_listas(lista1, lista2):
    lista_unicos = []
    i = 0
    if not lista2:
        lista_unicos.append(lista1)
        return lista_unicos
    while len(lista1) > 0:
        if lista1[0] != lista2[i]:
            lista_unicos.append(lista1[0])
            del(lista1[0])
            i = 0
        elif lista1[0] == lista2[i]:
            del(lista1[0])
            i += 1
        
    return lista_unicos