def monta_dicionario(chaves, valores):
    
    dicionario = {}
    
    for indice in range(len(chaves)):
        dicionario[chaves[indice]] = valores[indice]
    
    return dicionario