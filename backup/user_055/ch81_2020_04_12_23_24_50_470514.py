def interseccao_valores(dict_1, dict_2):
    values_1 = dict_1.values()
    values_2 = dict_2.values()
    lista_values = []

    for i in values_1:
        if i in values_1 and i in values_2:
            lista_values.append(i)
    return lista_values