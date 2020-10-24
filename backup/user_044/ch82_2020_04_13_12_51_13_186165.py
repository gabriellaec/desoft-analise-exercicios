def primeiras_ocorrencias(stg):
    dic={}
    for i in len(stg):
        for z in dic:
            if z!=stg[i]:
                dic[stg[i]]=int(i)
    return dic
               
        