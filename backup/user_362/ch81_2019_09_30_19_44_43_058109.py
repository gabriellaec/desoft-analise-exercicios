def interseccao_valores(dict1,dict2):
    lista=[]
    for v in dict1.values():
        if v in dict2:
            lista.append(v)
    return lista