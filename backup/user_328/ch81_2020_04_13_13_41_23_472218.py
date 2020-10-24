def interseccao_valores(dict1,dict2):
    lista1 = []
    for i in dict1.values():
        if i in dict2.values():
            lista1.append(i)
    return lista1
        