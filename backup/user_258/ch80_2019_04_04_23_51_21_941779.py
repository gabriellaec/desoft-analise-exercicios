def interseccao_chaves(dic1,dic2):
    lista=[]
    for e in dic1.keys():
        lista.append(e)
    for k in dic2.keys():
        if k not in lista:
            lista.append(k)
    return lista