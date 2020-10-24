def medias_por_inicial(d):
    d2 = {}
    
    for c in d:
        for k, v in c.items():
            d2[k[0]] = v
            
    return d2