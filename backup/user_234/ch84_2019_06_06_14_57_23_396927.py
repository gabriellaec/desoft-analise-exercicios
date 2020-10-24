def inverte_dicionario(dic):
    invert = {}
    for nome, idade in dic.items():
        invert[idade] = nome
    return invert