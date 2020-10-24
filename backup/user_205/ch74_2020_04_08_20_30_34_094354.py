def conta_bigramas(string):
    dic={}
    for i in range(len(string)-1):
        dic[string[i:i+2]]=string.count(string[i:i+2])
    return dic