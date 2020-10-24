def medias_por_inicial(dic):
    dicnovo={}
    for chave,valor in dic.items():
        for chave2,valor2 in dic.items():
            if chave[0]==chave2[0] and chave!=chave2:
                dicnovo[chave[0]]+= (valor2-valor)/2
    return dicnovo
        