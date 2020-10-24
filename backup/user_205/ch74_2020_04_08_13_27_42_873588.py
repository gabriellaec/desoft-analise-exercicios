def conta_bigramas(string):
    dic={}
    for i in (0,len(string),2):
        dic[i]=string.count(i)
    return dic
        