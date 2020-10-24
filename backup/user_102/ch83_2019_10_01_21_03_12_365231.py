def inverte_dicionario(dicionario):
    dicionarionovo = {}
    for a, b in dicionario.items():
        if a[0] in dicionarionovo:
            dicionarionovo[a[0]] = [9.5]
        else:
            dicionarionovo[a[0]] = [b]
    return dicionarionovo

