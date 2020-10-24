
def medias_por_inicial (dic_nomes):
    dic_media = {}
    for k,v in dic_nomes.items():  
        pri_letra = k[0] #primeira letra de cada key
        if pri_letra not in dic_media:
            dic_media[pri_letra] = v
        else:
            dic_media[pri_letra] = (dic_media[pri_letra] + v)/2
        
    return dic_media