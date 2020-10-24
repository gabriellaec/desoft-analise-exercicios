def inverte_dicionario (dic): 
    inverte = {}
    for valor,chave in dic.items():
        if not chave in inverte: 
            inverte[chave]=[valor]
        else:
            inverte[chave].append(valor)
    return inverte