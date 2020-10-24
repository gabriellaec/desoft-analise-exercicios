def medias_por_inicial(dic_notas):
    dic_iniciais={}
    for nome in dic_notas:
        inicial=nome[0]
        if inicial in dic_iniciais:
            dic_iniciais[inicial]=(dic_notas[nome]+dic_iniciais[inicial])/2
        
        else:
            dic_iniciais[inicial]=dic_notas[nome]
        
    return dic_iniciais