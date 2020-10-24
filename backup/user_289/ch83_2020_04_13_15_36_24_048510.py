def medias_por_inicial(dict_notas):
    dict_medias = {}
    for i, v in dict_notas.items():
        if not i[0] in dict_medias:
            dict_medias[i[0]] = [] 
        dict_medias[i[0]].append(v)
    for nomes, valores in dict_medias.items():
        valores = sum(valores)/len(valores)
        dict_medias[nomes] = valores
    
    return dict_medias