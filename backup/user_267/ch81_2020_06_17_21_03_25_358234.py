def interseccao_valores(dicio1, dicio2):
    lista_valores = []
    for i in dicio1.values():
        if i in dicio2.values():
            lista_valores.append(i)
    return lista_valores
            