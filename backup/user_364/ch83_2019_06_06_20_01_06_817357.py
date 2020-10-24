def medias_por_inicial(dic_notas):
    dic_final={}
    for k[0],v in dic_notas.items():
        novo_v=v
        v_antigo= dic_final[k[0]].values()
        if k[0] not in dic_final:
            dic_final[k[0]]=v
        else:
            dic_final[k[0]]=(v_antigo+novo_v)/2
    return dic