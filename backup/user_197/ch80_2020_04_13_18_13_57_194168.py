def interseccao_chaves(d1,d2):
    lista=[]
    for i in d1:
        if i in d2:
            lista.append(i)
    return lista
    