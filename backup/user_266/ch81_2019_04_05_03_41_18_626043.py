def interseccao_valores(D1,D2):
    lista=[]
    for v in D1.values():
        if v in D2.values():
            lista.append(v)
    return lista