def interseccao_chaves(dict1,dict2):
    lista=[]
    for k in dict1:
        if k in dict2:
            lista.append(k)
    return lista