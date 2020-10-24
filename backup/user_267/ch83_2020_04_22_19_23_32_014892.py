def medias_por_inicial(dicionotas):
    new = dict()
    i = 0
    for nome,nota in dicionotas.items():
        if nome[0] in new:
            new[nome[0]] += 1
        else:
            new[nome[0]] = 1
    return new

         