def interseccao_chaves(dic1,dic2):
    lista = []
    for i in dic1:
        for e in dic2:
            if e == i:
                lista.append(e)
    return lista
    