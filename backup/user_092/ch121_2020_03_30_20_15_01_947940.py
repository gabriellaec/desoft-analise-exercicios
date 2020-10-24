def subtracao_de_listas(lista1,lista2):
    lista0 = []
    i = 0
    if len(lista2) == 0:
        return lista1
    elif len(lista1) == 0:
        return lista1
    else:
        while(i <= len(lista1)):
            if lista1[i] not in lista2:
                lista0.append(lista1[i])
                i += 1
        return lista0