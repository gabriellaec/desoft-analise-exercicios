def medias_por_inicial(notas):
    dic={}
    for k,v in notas.items():
        dic[k[0]]=dic.get(k[0],[])
        dic[k[0]].append(v)
    return { sum(notas)/len(notas) for incial,notas in dic.items()}