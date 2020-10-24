def interseccao_valores(d1,d2):
    lista = []
    for i in d1.values():
        if i in d2.values():
            lista.append(i)
    return lista
