def medias_por_inicial(dic_nome):
    dic_inicial={}
    for i,j in dic_nome.items():
        if i[0] not in dic_inicial.keys():
            dic_inicial[i[0]]=j
        else:
            dic_inicial[i[0]]=dic_inicial[i[0]]/2+j/2
    return dic_inicial