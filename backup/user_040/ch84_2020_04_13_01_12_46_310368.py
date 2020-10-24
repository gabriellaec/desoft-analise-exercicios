def inverte_dicionario(x):
    dicionario = {}
    for nome,idade in x.items():
        if idade not in dicionario.keys():
            dicionario[idade] = "{0}".format(nome)
        else:
            dicionario[idade] = zip(dicionario[idade],"{0}".format(nome))
    return dicionario