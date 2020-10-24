def medias_por_inicial(dic):
    result = {}
    
    for key, value in dic.items():
        if key[0] in result:
            result[key[0]] = (result[key[0]] + value)/2
        else:
            result[key[0]] = value
    
    return result