def interseccao_chaves(dic1,dic2):
    lista = []
    for e in dic1:
        if e.keys() in dic2.keys():
            lista.append(e.keys())
        else:
            e = e
    return lista