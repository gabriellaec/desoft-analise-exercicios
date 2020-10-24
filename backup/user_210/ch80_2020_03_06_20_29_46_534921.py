def interseccao_chaves(l):
    dic1 = l[0]
    dic2 = l[1]
    lista = []
    for c in dic1:
        lista.append(dic1[c])

    for c in dic2:
        lista.append(dic2[c])
    return lista