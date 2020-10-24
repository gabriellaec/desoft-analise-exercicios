def inverte_dicionario(dic):
    invdict = {}
    for idade in dic.values():
        invdct[idade] = []
    for nome, idade in dic.items():
        invdict[idade].append(nome)
    return invdict