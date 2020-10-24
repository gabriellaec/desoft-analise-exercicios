def interseccao_chaves(dic1,dic2):
    lista = []
    k1 = dic1.keys()
    for e in k1:
        if e in dic2.keys():
            lista.append(e)
    return lista