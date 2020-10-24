def conta_bigramas(bigrama):
    cont=0
    dic={}
    while cont < len(bigrama)-1:
        bi=bigrama[cont]+bigrama[cont+1]
        if bi in dic:
            dic[bi]+=1
        else:
            dic[bi]=1
        cont+=1
    return dic