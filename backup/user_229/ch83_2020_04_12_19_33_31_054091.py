def medias_por_inicial(nomes):
    inicial = dict()
    contador = dict()
    for i in nomes:
        if i[0] not in inicial:
            inicial[i[0]] = nomes[i]
            contador[i[0]] = 1
        else:
            inicial[i[0]] += nomes[i]
            contador[i[0]] += 1
    for x in inicial:
        inicial[x] = inicial[x]/contador[x]
    return inicial