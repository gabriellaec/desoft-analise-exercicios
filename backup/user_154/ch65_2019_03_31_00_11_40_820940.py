def acha_bigramas(string):
    result = []
    
    i = 0
    
    while i < len(string) - 1:
        result.append(string[i] + string[i+1])
        i = i + 1
    return result