def interseccao_chaves(d1, d2):
    lista=[]
    for k1 in d1.items():
        lista.append(k1)
    for k2 in d2.items():
        lista.append(k2)
    return lista