def medias_por_inicial(dict):
    dictnovo={}
    c=1
    for k,v in dict.items():
        if k[0] not in dictnovo:
            dictnovo[k[0]]=v
        else:
            c+=1
            dictnovo[k[0]]=(dictnovo[k[0]]+v)/c
    return dictnovo