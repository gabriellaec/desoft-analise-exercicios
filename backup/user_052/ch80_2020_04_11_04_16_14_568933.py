def interseccao_chaves (dic1, dic2):
    lista = []
    for i in dic1.keys():
        for a in dic2.keys():
            if a == i:
                lista.append([a])
    return lista
                