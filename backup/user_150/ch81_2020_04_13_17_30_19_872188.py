def interseccao_valores(dic1, dic2):
    lista = []
    for v in dic1.values() and v in dic2.values():
        lista.append(v)
    return lista