def interseccao_chaves(dic1, dic2):
    lista = []
    chaves = dic1.keys()
    chaves2 = dic2.keys()
    for e in chaves:
        lista.append(e)
    for c in chaves2:
        lista.append(c)
    return lista