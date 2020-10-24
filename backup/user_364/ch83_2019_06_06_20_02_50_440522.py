def medias_por_inicial(dic_notas):
    dic_final={}
    for k,v in dic_notas.items():
        dic[k[0]]=v
        for m,n in dic_notas.items():
            if k[0]== m[0] and k != m:
                dic[k[0]] += (n-v)/2
    return dic