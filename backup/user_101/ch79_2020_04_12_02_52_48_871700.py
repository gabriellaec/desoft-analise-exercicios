def monta_dicionario(chaves, elementos):
    dic = {}
    for i, e in enumerate(chaves):
        dic[e] = elementos[i]
    return dic