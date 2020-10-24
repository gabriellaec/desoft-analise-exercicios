def interseccao_chaves(dic1, dic2):
    lista=[]
    for i in dic1.keys():
        for k in dic2.keys():
            if i==k:
                lista.append(i)
    return lista