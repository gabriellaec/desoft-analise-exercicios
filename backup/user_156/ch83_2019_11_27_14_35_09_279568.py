def medias_por_inicial(x):
    saida = {}
    
    for k,v in x.items():
        if k[0] not in saida.keys():
            saida[k[0]] = v
    return saida
        
    
    