def conta_bigramas(palavra):
    dic={}
    for e in palavra:
        lista=[e,e+1]
        stringeras=''.join(lista)
        if stringeras in dic:
            dic[stringeras]+=1
        else:
            dic[stringeras]=1
    return dic