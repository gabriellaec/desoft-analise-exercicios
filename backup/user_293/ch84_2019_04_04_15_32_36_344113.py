def inverte_dicionario(dic):
    nomes = list(dic.keys())
    idades = set(list(dic.values()))
    newdic = dict(zip(idades,nomes))
    return newdic
        