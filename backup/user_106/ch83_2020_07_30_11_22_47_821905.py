def medias_por_inicial(nomes):
    iniciais = {}
    for n in nomes:
        if not n[0] in iniciais:
            iniciais[n[0]] = nomes[n]
        else:
            iniciais[n[0]] += nomes[n]
    for i in iniciais:
        c = 0
        for n in nomes:
            if n[0] == i:
                c += 1
        iniciais[i] = iniciais[i] / c
    return iniciais