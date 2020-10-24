def medias_por_inicial(dic):
    dicIniciais={}
    Dic={}
    for a in dic.keys():
        inicial=a[0]
        if inicial not in dicIniciais.keys():
            dicIniciais[inicial]=1
        else:
            dicIniciais[inicial]+=1
    for b,c in dic.items():
        inicial=b[0]
        if inicial not in Dic.keys():
            Dic[inicial]=c
        else:
            Dic[inicial]+=c
    for t,v in Dic.items():
        inicial=t[0]
        n=dicIniciais[inicial]
        v=v/n
        Dic[inicial]=v
    return Dic
            
        