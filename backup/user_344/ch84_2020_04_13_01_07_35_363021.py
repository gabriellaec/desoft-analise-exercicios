def inverte_dicionario(dic):
    chaves = list(dic.keys())
    valores = list(dic.values())
    dicionario = dict(zip(valores,chaves))
    return dicionario
    
