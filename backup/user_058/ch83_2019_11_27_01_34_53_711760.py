def medias_por_inicial(dicionario):
    ocorrencia = {}
    media = {}
    for k,v in dicionario.items():
        lista = list(k)
        primeira = lista[0]
        if primeira not in ocorrencia.keys():
            ocorrencia[primeira] = v/2
        elif primeira in ocorrencia.keys():
            ocorrencia[primeira] += v/2
            
    for k,v in ocorrencia.items():
        media[k] = v
    return media