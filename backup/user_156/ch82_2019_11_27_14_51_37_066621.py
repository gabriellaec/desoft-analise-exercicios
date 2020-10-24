def primeiras_ocorrencias(x):
    saida = {}
    
    for e in range(len(x)):
        if x[e] not in saida.keys():
            saida[x[e]] = e
    return saida
        
        
        
    