def interseccao_chaves(dic1,dic2):
    lista=[]
    for t in dic1.keys():
        if t in dic2.keys():
            lista.append(t)
    return lista
            