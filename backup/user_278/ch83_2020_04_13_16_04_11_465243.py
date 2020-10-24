def medias_por_inicial (dic_nomes):
    soma = {}
    quantidade = {}
    for k,v in dic_nomes.items():  
        pri_letra = k[0] #primeira letra de cada key
        if pri_letra in soma:
            soma [pri_letra] += v
            quantidade [pri_letra] += 1
        else:
            soma[pri_letra] = v
            quantidade [pri_letra] = 1
    dic_media = {}
    for k,v in soma.items():
        q = quantidade[k]
        dic_media [k] = v/q
    return dic_media