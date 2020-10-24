def interseccao_chaves(dic1, dic2):
    lista=[]
    for i in dic1.items():
        lista.append(i)
    for k in dic2.items():
        lista.append(k)
    return lista