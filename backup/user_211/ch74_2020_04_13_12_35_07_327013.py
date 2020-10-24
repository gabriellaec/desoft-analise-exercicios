def conta_bigramas(string):
    dic= {}
    i=0
    for i in range(len(string)-1):
        bigrama= string[i] + string[i+1]
        if bigrama not in dic:
            dic[bigrama] = 1
        else:
            dic[bigrama] += 1
        
    return dic