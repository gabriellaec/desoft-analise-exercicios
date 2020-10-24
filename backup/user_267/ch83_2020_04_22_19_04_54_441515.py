def medias_por_inicial(dicionotas):
    soma = 0
    termos = 0
    new = dict()
    i = 0
    for nome,nota in dicionotas.items():
        if nome[0] == [i+1]:
            soma += dicionotas[i] + dicionotas[i+1]
            termos += 1
            i += 1
        media = soma/termos
        new[i] = media
    return new
            