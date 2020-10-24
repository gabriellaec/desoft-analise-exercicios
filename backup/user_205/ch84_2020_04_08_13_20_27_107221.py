def inverte_dicionario (dic): 
    inverte = {}
    for chave,valor in dic.items():
        inverte[valor]=chave
    return inverte