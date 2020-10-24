def medias_por_inicial(dicionario):
    new_dic={}
    dic_oco={}
    dic_final={}
    for nome, nota in dicionario.items():
        primeira_letra=nome[0]
        if primeira_letra not in new_dic:
            new_dic[primeira_letra]=0
        if primeira_letra not in dic_oco:
            dic_oco[primeira_letra]=0
        dic_oco[primeira_letra]+=1
        new_dic[primeira_letra]+=nota
        for soma in new_dic.values():
            for ocorrencia in dic_oco.values():
                vtotal=soma/ocorrencia
                if vtotal not in dic_final.items():
                    dic_final[primeira_letra]=vtotal
    return dic_final
