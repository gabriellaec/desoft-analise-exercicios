def medias_por_inicial(nomes):
    iniciais = {}
    for n in nomes:
        if not n[0] in iniciais:
            iniciais[n[0]] = nomes[n]
        else:
            iniciais[n[0]] += nomes[n]
    return iniciais