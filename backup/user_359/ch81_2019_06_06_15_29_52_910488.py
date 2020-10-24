def interseccao_valores(dict1,dict2):
    lista_val = list()
    for v1 in dict1.values():
        lista_val.append(v1)
    for v2 in dict2.values():
        lista_val.append(v2)
    return lista_val
    