def interseccao_valores(dic1,dic2):
    lista = []
    for i in dic1.values():
        for x in dic2.values():
            if x == i:
                lista.append(i)
    return lista