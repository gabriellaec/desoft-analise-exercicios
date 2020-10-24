def medias_por_inicial(notas):
    nomes = {}
    for k, v in notas.items():
        nomes[k[0]] = v
        for m, n in notas.items():
            nomes[k[0]] += (n-v)/2
    return nomes