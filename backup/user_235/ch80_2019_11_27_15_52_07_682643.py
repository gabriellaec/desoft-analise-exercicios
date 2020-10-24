def interseccao_chaves(dict1,dict2):
    lista=[]
    for i in dict1:
        if i in dict2:
            lista.append(i)
    return lista