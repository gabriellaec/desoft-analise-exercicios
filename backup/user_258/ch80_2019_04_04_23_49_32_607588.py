def interseccao_chaves(dic1,dic2):
    lista=[]
    for e in dic1.keys():
        lista.append(e)
    for k in dic2.keys():
        lista.append(k)
    return lista