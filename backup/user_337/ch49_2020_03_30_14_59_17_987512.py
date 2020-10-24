def inverte_lista(lista):
    i = len(lista)
    list2 = lista[i:0:-1]
    list2.append(lista[0])
    return list2