def subtracao_de_listas(lista1, lista2):
    lista_unicos = []
    i = 0
    while len(lista1) >= 0:
        if lista1[0] == lista2[i]:
            lista_unicos.append(lista[0])
            del(lista1[0])
            i = 0
        elif i == len(lista2):
            break
        else:
            i += 1
    return lista_unicos