def interseccao_chaves(dic1,dic2):
    lista = []
    for e in dic1:
        if dic1.keys() in dic2.keys():
            lista.append(dic1.keys())
        else:
            e = e
    return lista