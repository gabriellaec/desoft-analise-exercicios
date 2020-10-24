def medias_por_inicial (dic_nomes):
    dic_media = {}
    conta = 1
    for k,v in dic_nomes.items():  
        pri_letra = k[0] #primeira letra de cada key
        if pri_letra not in dic_media:
            dic_media[pri_letra] = v
        else:
            conta += 1
            dic_media[pri_letra] = (dic_media[pri_letra] + v)
            
    for i in dic_media.keys():
        dic_media[i] = dic_media[i]/conta
        
    return dic_media