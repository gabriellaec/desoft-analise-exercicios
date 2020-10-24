def interseccao_valores(dict1,dict2):
    lista=[]
    for c in dict1.values():
        if c in dict1.values() and dict2.values():
            lista.append(c)
    return lista
