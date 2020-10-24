def conta_bigramas (palavra):
    dic={}
    bigramas=[]
    i=0
    while i<len (palavra)-1:
        bigramas.append (palavra[i]+palavra[i+1])
        i+=1
    for bigrama in bigramas:
        if bigrama not in dic:
            dic[bigrama]=1
        else:
            dic[bigrama]=dic[bigrama]+1
    return dic
    