def interseccao_valores(dic1, dic2):
    lista = []
    for v in dic1.values():
        v.append(lista)
    for j in dic2.values():
        j.append(lista)
    return lista
    