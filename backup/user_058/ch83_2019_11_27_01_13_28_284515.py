def medias_por_inicial(dicionario):
    ocorrencia = {}
    for k,v in dicionario.items():
        lista - list(k)
        primeira = lista[0]
        if primeira not in ocorrencia.keys():
            ocorrencia[primeira] = v
        elif primeira in ocorrencia.keys():
            ocorrencia[primeira] += v
    for k,v in media.items():
        media[k] = v/2
    return media