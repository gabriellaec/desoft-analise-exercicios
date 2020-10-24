def medias_por_inicial(dicionotas):
    new = dict()
    for nome,nota in dicionotas.items():
        a = nome[0]
        if a in new:
            new[a] += 1
        else:
            new[a] = 1
    return new

         