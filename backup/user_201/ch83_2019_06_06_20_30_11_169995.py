def medias_por_inicial(dic):
    dicIniciais={}
    Dic={}
    for a in dic.keys():
        inicial=a[0]
        if inicial not in dicIniciais:
            dicIniciais[inicial]=1
        else:
            dicIniciais[inicial]+=1
    for b,c in dic.items():
        inicial=b[0]
        if inicial not in Dic:
            Dic[inicial]=c
        else:
            Dic[inicial]+=c
    for t,v in Dic.items():
        v=v/dicIniciais[t]
    return Dic
            
        