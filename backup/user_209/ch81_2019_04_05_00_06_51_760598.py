def interseccao_chaves (dicobas,dicoberas):
    lista = []
    for e in dicobas.values():
        for i in dicoberas.valeus():
            if i == e:
                lista.append (e)
    return lista