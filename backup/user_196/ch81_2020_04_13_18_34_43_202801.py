def interseccao_valores(dic1,dic2):
    lista = []
    for a in dic1.values():
        if a in dic2.values():
            lista.append(a)
    return lista
