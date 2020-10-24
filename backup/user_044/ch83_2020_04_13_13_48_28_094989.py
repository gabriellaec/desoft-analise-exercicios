def medias_por_inicial(dic):
    dn={}
    num={}
    for i,n in dic.items():
        if i[0] not in dn:
            dn[i[0]]=n
            num[i[0]]=1
        else:
            dn[i[0]]=num[i[0]]*dn[i[0]]+n
            num[i[0]]+=1
            dn[i[0]]=dn[i[0]]/num[i[0]]
                    
    return dn