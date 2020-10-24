def interseccao_valores (d1,d2):
    valores = d1.values()
    lista = []
    for i in valores:
        if i in d2.values:
            lista.append(i)

    return lista                