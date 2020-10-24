def interseccao_chaves(dic1,dic2):
    lista = []
    for k in dic1:
        if k in dic2:
            lista.append(k)
    return lista