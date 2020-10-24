def interseccao_chaves(dict1,dict2):
    lista_key = list()
    lista_cor = list()
    for k1 in dict1.keys():
        lista_key.append(k1)
    for k2 in dict2.keys():
        lista_key.append(k2)
    for i in lista_key:
        if i in dict1.keys() and i in dict2.keys():
            if i not in lista_cor:
            	lista_cor.append(i)
    return lista_cor