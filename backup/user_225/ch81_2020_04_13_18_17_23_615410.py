def interseccao_valores(dic1, dic2):
    lista = []
    valores = dic1.values()
    valores2 = dic2.values()
    for e in valores:
        if e in valores2:
            lista.append(e)
    return lista