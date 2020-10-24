def acha_bigramas(string):
    result = []  
    bigrama = []
    
    for x in string:
        bigrama.append(x)
        if len(bigrama) == 2:
            result.append(bigrama)
            bigrama = []
    if len(bigrama) != 0:
        result.append(bigrama)
    return result