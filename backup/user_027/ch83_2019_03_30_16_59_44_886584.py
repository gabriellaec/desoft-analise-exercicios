def medias_por_inicial(x):
    ocorrencias = {}
    somas_notas = {}
    saida = {}
    for i in x:
        if i[0] in ocorrencias:
            ocorrencias[i[0]] += 1
            somas_notas[i[0]] += x[i]
        else:
            ocorrencias[i[0]] = 1
            somas_notas[i[0]] = x[i]

    for i in ocorrencias:
        saida[i] = somas_notas[i]/ocorrencias[i]
    return saida