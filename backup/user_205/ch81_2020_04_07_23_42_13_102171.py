def interseccao_valores(dic1,dic2):
    lista = []
    for valor in dic1.values:
        for valor2 in dic2.values:
            if valor==valor2:
                lista.append(valor)
    return lista