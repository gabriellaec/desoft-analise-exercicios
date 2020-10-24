def conta_bigramas(string):
    result = {}
    
    for i in range(len(string) - 1):
        item = string[i:(i+2)]
        
        if item in result:
            result[item] =  result[item] + 1
        else:
             result[item] = 1
    
    return result