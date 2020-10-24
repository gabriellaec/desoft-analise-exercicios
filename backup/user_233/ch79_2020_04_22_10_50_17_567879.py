def monta_dicionario(chaves, valores):
    
    dicionario = {}
    
    for indice in range(len(chaves)):
        dicionario[chaves[indice]] = chaves[indice]
    
    return dicionario