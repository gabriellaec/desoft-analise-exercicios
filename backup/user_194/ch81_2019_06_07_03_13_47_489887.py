def interseccao_valores(dic1,dic2):
    lista = []
    for v in dic1.values():
        for valores in dic2.values():
            if valores == v and v not in lista:
                lista.append(v)
    return lista