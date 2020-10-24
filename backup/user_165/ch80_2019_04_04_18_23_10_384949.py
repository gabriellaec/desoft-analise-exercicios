def interseccao_chaves(dic_1,dic_2):
    lista = []
    for e in dic_1:
        for i in dic_2:
            if e == i:
                lista.append(e)
    return lista    