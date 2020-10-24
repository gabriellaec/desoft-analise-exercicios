def medias_por_inicial(alunos_notas):
    notas = {}
    ocorrencias = {}
    media_notas = {}
    for k, v in alunos_notas.items():
        if k[0] not in notas:
            notas[k[0]] = v
            ocorrencias[k[0]] = 1
        else:
            notas[k[0]] += v
            ocorrencias[k[0]] += 1
    for k, v in notas.items():
        o = ocorrencias[k]
        media_notas[k] = v/o
    return media_notas