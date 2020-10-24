def inverte_dicionario(dicionario):
    novo_dicio = dict()
    for nome in dicionario:
        if dicionario[nome] not in novo_dicio:
            lista = []
            lista.append(diconario.key())
            novo_dicio[dicionario[nome]] = lista
        else:
            lista.append(diconario.key())
            novo_dicio[dicionario[nome]] = lista
    return novo_dicio
            