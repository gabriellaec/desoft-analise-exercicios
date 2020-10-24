def medias_por_inicial(dicionario):
    new_dic={}
    for nome, nota in dicionario.items():
        primeira_letra=nome[0]
        if primeira_letra not in new_dic:
            new_dic[primeira_letra]=0
        new_dic[primeira_letra]+=nota        
    return new_dic
print(medias_por_inicial(dicionario))
        