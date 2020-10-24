def interseccao_valores(dict1,dict2):
    v = dict1.values
    v2 = dict2.values
    lista1 = []
    
    for k in v:
        lista1.append(k)
    for i in v2:
        lista1.append(i)
    return lista1