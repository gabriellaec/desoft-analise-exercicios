def interseccao_chaves(d1, d2):
    lista=[]
    for k1 in d1: 
        for k2 in d2:
            if k1==k2:
                lista.append(k1)
    return lista