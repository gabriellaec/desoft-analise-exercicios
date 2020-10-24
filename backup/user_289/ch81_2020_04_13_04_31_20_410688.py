def interseccao_valores(dict1, dict2):
    lista_i = []
    lista_1 = []
    lista_2 = []
    for i in dict1.values():
        lista_1.append(i)
    for e in dict2.values():
        lista_2.append(e)
    for elemento i in lista_1:
        if elemento in lista_2:
            lista_interseccao.append(elemento)
    return lista_interseccao