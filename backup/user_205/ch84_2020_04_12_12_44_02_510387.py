def inverte_dicionario (dic): 
    inverte = {}
    for valor,chave in dic.items():
        if not chave in inverte: 
            inverte[chave]=[valor]
        else:
            inverte[chave].append(valor)
    return inverte

#Segunda forma, treino prova 

def inverte_dicionario(dicionario):
    resultado = {}
    for chave,valor in dicionario.items():
        if valor not in resultado:
            resultado[valor]=[chave]
        else:
            resultado[valor]+=[chave]
    return resultado