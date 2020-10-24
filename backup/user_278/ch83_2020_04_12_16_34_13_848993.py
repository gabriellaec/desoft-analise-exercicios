def medias_por_inicial (dic_nomes):
    dic_media = {}
    for k in dic_nomes:  #percorre keys
        pri_letra = k[0] #primeira letra de cada key
        if pri_letra not in dic_media:
            dic_media[pri_letra] = dic_nomes[k]
        else:
            dic_media[pri_letra] = (dic_media[pri_letra] + dic_nomes[k])/2
    return dic_media