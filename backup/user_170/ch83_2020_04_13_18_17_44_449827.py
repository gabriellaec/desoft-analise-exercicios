def medias_por_inicial(nome_notas):
    inicial = {}

    for i, n in nome_notas.items():
        if not i[0] in inicial:
            inicial[i[0]] = [n]
        else:
            inicial[i[0]].append(n)
    for i, n in inicial.items():
        inicial[i] = sum(n)/len(n)
    return inicial