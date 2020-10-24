def conta_bigramas (string):
    i=1
    u=0
    dic={}
    while u<len(string):
        if (string[i] + string[u]) in dic:
            values = string.count(string[i]+string[u])
            dic[string[i]+string[u]] = values
        else:
            dicionario[string[i]+string[u]] = 1
        i+=1
        u+=1

    return dic 
            
    