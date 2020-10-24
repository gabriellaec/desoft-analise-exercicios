def conta_bigramas(string):
    dic = {}
    for bi in string:
        if not bi in string:
            dic[bi] = 1
            
        else:
            dic[bi] += 1
    return dic
        
        
    