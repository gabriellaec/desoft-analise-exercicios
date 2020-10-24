def conta_bigramas(palavra):
    dicionario = {}
    
    i = 0
    
    while i < len(palavra)-1:
        
        bigrama = palavra[i] + palavra[i + 1]
        
        if bigrama in dicionario:
            
            dicionario[bigrama] += 1
            
        else:
            
            dicionario[bigrama] = 1
            
        i += 1
        
    return dicionario
        