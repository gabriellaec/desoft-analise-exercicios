def interseccao_valores(dict1,dict2):
    lista_val = list()
    lista_cor = list()
    for v1 in dict1.values():
        lista_val.append(v1)
    for v2 in dict2.values():
        lista_val.append(v2)
    for i in lista_val:
        if i in dict1.values() and i in dict2.values():
            if i not in lista_cor:
            	lista_cor.append(i)
    return lista_cor
    