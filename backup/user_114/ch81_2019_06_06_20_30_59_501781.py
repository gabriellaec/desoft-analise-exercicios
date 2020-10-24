def interseccao_valores(dict1,dict2):
    lista=[]
    for v1 in dict1.values():
        for v2 in dict2.values():
            if v1==v2:
                lista.append(v1)
    return lista