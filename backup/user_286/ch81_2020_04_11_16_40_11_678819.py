def interseccao_valores(dic_1, dic_2):
    lista_valores = []
    for valor in dic_1.values():
        lista_valores.append(valor)
    for valor in dic_2.values():
        if valor not in dic_1.values():
            lista_valores.append(valor)

    return lista_valores