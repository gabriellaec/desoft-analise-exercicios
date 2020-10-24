def conta_bigramas(string):
    dic = {}
    for bi in string:
        if bi in dic:
            dic[bi] += 1 
            
        else:
            dic[bi] = 1
    return dic