def interseccao_chaves(dic1, dic2):
    lista = []
    for e in dic1.keys():
        lista.append(e)
    for i in dic2.keys():
        lista.append(i)
    return lista