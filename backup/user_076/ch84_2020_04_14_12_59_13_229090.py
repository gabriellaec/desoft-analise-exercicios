def inverte_dicionario (d1):
    d2 = {}
    for i in d1:
        if i not in d2:
            lista = []
            d2[d1[i]] = lista.append(i)
        else:
            d2[d1[i]] = lista.append(i)
    return d2