def interseccao_chaves(dic1,dic2):
    lista = []
    for k in dic1.keys():
        if k in dic2.keys():
            lista.append(k)
    return lista