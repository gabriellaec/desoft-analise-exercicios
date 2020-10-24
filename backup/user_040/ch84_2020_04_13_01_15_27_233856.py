def inverte_dicionario(x):
    dicionario = {}
    for nome,idade in x.items():
        if idade not in dicionario.keys():
            dicionario[idade] = ["{0}".format(nome)]
        else:
            dicionario[idade] = dicionario[idade].append("{0}".format(nome))
    return dicionario