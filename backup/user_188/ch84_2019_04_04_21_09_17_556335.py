def inverte_dicionario(dic):
    invdict = {}
    for nome, idade in dic.items():
        invdict[idade] = nome
    return invdict