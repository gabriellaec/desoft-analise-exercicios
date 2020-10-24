def conta_bigramas(string):
    dic={}
    for i in (0,len(string)-1,2):
        dic[string[i]]=string.count(string[i])
    return dic
        