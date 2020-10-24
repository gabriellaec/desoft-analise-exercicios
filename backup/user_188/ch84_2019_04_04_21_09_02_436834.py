def inverte_dicionario(dict):
    invdict = {}
    for nome, idade in dict.items():
        invdict[idade] = nome
    return invdict