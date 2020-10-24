def medias_por_inicial (dic):
    dicnovo = {}
    for nome,media in dic.items ():
        inicial = nome[0]
    	dicnovo[inicial] = media
    return dicnovo