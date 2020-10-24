def interseccao_chaves (dicobas,dicoberas):
    lista = []
    for e in dicobas.keys():
        for i in dicoberas.keys():
            if i == e:
                lista.append (e)
    return lista