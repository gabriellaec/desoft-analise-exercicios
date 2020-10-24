def inverte_dicionario(dicionario):
    d={}
    for idades in dicionario.values():
        d[idades]=1
    for nomes in dicionario:
        if nomes not in d:
            d[idades]=nomes
    return d