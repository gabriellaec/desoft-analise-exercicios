def inverte_dicionario(x):
    dicionario = {}
    for nome in x.keys():
        for idade in x.values():
            if idade not in dicionario:
                dicionario[idade] = nome
            else:
                dicionario[idade] += nome
    return dicionario