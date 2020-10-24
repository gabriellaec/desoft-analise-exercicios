def conta_bigramas(palavra):
    dic={}
    for e in range(len(palavra)-1):
        lista=[palavra[e],palavra[e+1]]
        stringeras=''.join(lista)
        if stringeras in dic:
            dic[stringeras]+=1
        else:
            dic[stringeras]=1
    return dic