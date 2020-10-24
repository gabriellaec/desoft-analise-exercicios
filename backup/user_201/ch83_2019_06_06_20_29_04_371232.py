def medias_por_inicial(dic):
    dicIniciais={}
    Dic={}
    for a in dic.keys():
        a[0]=inicial
        if inicial not in dicIniciais:
            dicIniciais[inicial]=1
        else:
            dicIniciais[inicial]+=1
    for b,c in dic.items():
        b[0]=inicial
        if inicial not in Dic:
            Dic[inicial]=c
        else:
            Dic[inicial]+=c
    for t,v in Dic.items():
        v=v/dicIniciais[t]
    return Dic
            
        