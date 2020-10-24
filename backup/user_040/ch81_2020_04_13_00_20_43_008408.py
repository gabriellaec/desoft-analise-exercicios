def interseccao_valores(x,y):
    lista = []
    for valor in x.values():
        for valor2 in y.values():
            if valor == valor2:
                lista.append(valor)
    return lista