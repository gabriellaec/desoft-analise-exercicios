def inverte_dicionario(dic):
    result = {}
    
    for key, value in dic.items():
        if key in result:
            result[value] = result[value] + key
        else:
            result[value] = key
    
    return result