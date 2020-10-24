def primeiras_ocorrencias(stg):
    dic={}
    for i in range(len(stg)):
        if stg[i] not in dic.keys():
            dic[stg[i]]=i
    return dic
               
        