def primeiras_ocorrencias(string):
    result = {}
    
    i = 0
    
    while i < len(string):
        if string[i] not in result:
            result[string[i]] = i
    
    return result