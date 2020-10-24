def medias_por_inicial(dic_nome):
    dic_inicial={}
    for i,j in dic_nome.items():
        dic_inicial[i[0]]=j
    return dic_inicial