def interseccao_chaves(D1,D2):
    lista=[]
    for k in D1.keys():
        if k in D2.keys():
            lista.append(k)
    return lista