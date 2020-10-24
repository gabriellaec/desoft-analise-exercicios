def interseccao_valores (dicobas,dicoberas):
    lista = []
    for e in dicobas.values():
        for i in dicoberas.values():
            if i == e:
                lista.append (e)
    return lista