def inverte_dicionario(dicionario):
    d={}
    for nomes,idades in dicionario.items():
        if nomes not in d:
            d[idades]=nomes
    return d