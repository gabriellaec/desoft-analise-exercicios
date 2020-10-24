def acha_bigramas(string):
    result = []
    
    for i in range(len(string) - 1):
        item = string[i:(i+2)]
        if item not in result:
            result.append(item)
            
    return result