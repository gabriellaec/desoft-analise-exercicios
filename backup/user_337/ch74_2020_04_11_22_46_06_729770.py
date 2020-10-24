def conta_bigramas(palavra):
    dic = {}
    i = 0
    while i<len(string)-1:
        a = string[i]+string[i+1]
        if not a in dic:
            dic[a]=1
        else:
            dic[a]+=1
        i+=1
    return dic
       
