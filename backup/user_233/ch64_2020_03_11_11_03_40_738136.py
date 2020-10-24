def acha_bigramas(string):
    
    bigramas = []
    
    for i in range(len(string) - 1):
        bigramas.append(string[i : i + 2])
        
    return bigramas