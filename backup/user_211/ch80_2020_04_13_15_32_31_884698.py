def interseccao_chaves(dic1,dic2):
    lista=[]
    for i in dic1.keys():
        if i in dic2.keys():
            lista.append(i)
    return lista