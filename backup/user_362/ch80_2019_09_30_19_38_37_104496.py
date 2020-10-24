def interseccao_chaves(dict1,dict2):
    lista=[]
    for i in dict1:
        if dict1[i]==dict2[i]:
            lista.append(i)
    return lista