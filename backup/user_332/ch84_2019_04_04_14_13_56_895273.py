def inverte_dicionario(dic):
    niver = {}
    for n, i in dic.items():
        if i in niver:
            lista.append(n)
        else:
            lista = [n]
        niver[i] = n
    return niver
