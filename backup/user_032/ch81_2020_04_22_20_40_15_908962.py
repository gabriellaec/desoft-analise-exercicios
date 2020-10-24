def interseccao_valores(dic1,dic2):
    lista = []
    for x in dic1.values():
        for y in dic2.values():
            if x == y:
                lista.append(x)
    return lista