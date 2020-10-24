def inverte_dicionario(dicionario):
    dicionarionovo = {}
    for a, b in dicionario.items():
        if b in dicionario:
            dicionarionovo[b].append(a)
        dicionarionovo[b]= [a]
    return dicionarionovo
