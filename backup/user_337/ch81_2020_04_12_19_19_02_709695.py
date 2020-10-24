def interseccao_chaves(dic1, dic2):
    lista = []
    for i in dic1.values():
        if i in dic2.values():
            lista.append(i)
    for i in dic2.values():
        if not i in lista:
            if i in dic1.values():
                lista.append(i)
    return lista