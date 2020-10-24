def inverte_dicionario(dicio):
    dicionew = dict()
    for nome in dicio:
        idade = dicio[nome]
        if idade in dicionew:
            dicionew[idade].append(nome)
        else:
            dicionew[idade] = [nome]
    return dicionew
