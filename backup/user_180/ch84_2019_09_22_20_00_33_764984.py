def inverte_dicionario(dicionario):
    for a, b in dicionario.items():
        dicionarionovo[b] = [a]
    return dicionarionovo