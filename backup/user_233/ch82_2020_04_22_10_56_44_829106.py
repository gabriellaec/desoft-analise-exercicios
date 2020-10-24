def primeiras_ocorrencias(string):
    
    dicionario = {}
    
    for indice in range(len(string)):
        
        caracter = string[indice]
        
        if caracter not in dicionario.keys():
            dicionario[caracter] = indice
    
    return dicionario