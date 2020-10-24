def interseccao_chaves(d1,d2):
    lista=[]
    for e in d1.keys():
        if e==d2.keys():
            lista.append(e)
    return lista