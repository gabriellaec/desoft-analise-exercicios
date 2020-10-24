def interseccao_chaves(dic1,dic2):
    k=dic1.keys()
    k2=dic2.keys()
    lista=[]
    for i in k:
        if i in k2:
            lista.append(i)
    return lista
    