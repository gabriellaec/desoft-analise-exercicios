def inverte_dicionario(x):
    dicionario = {}
    for nome,idade in x.items():
        if idade not in dicionario:
            dicionario[idade] = [nome]
        else:
            dicionario[idade] = zip(dicionario[idade],nome)
    return dicionario