def medias_por_inicial(d):
    d2 = {}
    
    for k, v in d:
        d2[k[0]] = v
        
    return d2