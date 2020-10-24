def inverte_dicionario(dic):
    nomes = list((dic.keys())
    idades = list(dic.values())
    newdic = dict(zip(idades,nomes))
    return newdic
        