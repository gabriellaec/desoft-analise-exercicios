def conta_bigramas(palavra):
    dicionario = {}
    
    i = 1
    
    t = 1
    
    for e in palavra:
        bigrama = e + palavra[i]
        if bigrama in dicionario:
            dicionario[e] = 1
        else:
            t += 1
            dicionario[e] = t
        i += 1
        
    return dicionario
        