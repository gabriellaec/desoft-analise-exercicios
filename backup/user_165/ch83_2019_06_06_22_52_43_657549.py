def medias_por_inicial(dicionario):
    dicionario_novo = {}
    dicionario_final = {}
    for nome,notas in dicionario.items():
            inicial = nome[0]
            if inicial not in dicionario_novo.keys():
                dicionario_novo[inicial] = [notas]
            else:
                dicionario_novo[inicial].append[notas]
    for notas in dicionario_novo:
        valores = dicionario[inicial]
        i = 0
        s = 0
        while i <len(valores):
            soma+=valores[i]
        media = s/i
        dicionario_final[inicial]=media
    return dicionario_final