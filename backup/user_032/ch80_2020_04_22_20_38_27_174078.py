def interseccao_chaves(dic1,dic2):
    lista = []
    for x in dic1.keys():
        for y in dic2.keys():
            if x == y:
                lista.append(x)
    return lista