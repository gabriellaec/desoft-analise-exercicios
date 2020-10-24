def inverte_dicionario(dic):
    k1 = dic.keys()
    v1 = dic.values()
    novo = {}
    x = 0
    for e in v1:
        novo[e] = x
    for n in k1:
        x = n
    return novo  