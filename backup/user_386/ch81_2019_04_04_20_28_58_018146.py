def interseccao_valores(dic1,dic2):
    lista = []
    c = dic2.values()
    for v in dic1.values():
        if v in c:
            lista.append(v)
    return lista