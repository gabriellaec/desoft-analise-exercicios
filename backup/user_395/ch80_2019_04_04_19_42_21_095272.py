def interseccao_chaves(dict1,dict2):
    lista = []
    for e in dict1:
        for i in dict2:
            if e == i:
                lista.append(e)
    return lista