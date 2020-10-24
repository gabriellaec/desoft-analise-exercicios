def monta_dicionario(chaves, valores):
    
    dicionario = {}
    
    for indice in range(len(chaves)):
        dicionario[chaves[indice]] = chaves[indice]
    
    return dicionario

print(monta_dicionario(['A', 'B', 'C'], [1,2,3]))