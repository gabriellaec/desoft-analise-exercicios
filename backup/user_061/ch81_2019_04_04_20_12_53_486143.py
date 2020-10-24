def interseccao_valores(dict1,dict2):
    lista = []
    for valor1 in dict1.values():
        for valor2 in dict2.values():
            if valor1 == valor2:
                lista.append(valor1)
    return lista