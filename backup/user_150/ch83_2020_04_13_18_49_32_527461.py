def medias_por_inicial(dicionario):
    dicionario2 = {}
    dicionario_count = {}
    for i in dicionario:
        if i[0] not in dicionario2:
            dicionario2[i[0]] = dicionario[i]
            dicionario_count[i[0]] = 1
        else:
            dicionario2[i[0]] += dicionario[i]
            dicionario_count[i[0]] += 1
    
    for k, v in dicionario2.items():
        dicionario2[k] = v / dicionario_count[k]
    return dicionario2