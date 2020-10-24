def interseccao_chaves(dic, dic2):
    lista = []
    for k in dic.keys():
        lista.append(k)
    for j in dic2.keys():
        lista.append(j)
    return lista