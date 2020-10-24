def interseccao_chaves(dic1, dic2):
    lista = []
    for i in dic1:
        if i in dic2:
            lista.append(i)
    for i in dic2:
        if not i in lista:
            if i in dic1:
                lista.append(i)
    return lista