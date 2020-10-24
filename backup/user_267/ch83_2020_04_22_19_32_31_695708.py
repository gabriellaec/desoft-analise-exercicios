def medias_por_inicial(dicionotas):
    new = dict()
    conta = {}
    for nome,nota in dicionotas.items():
        a = nome[0]
        if a in new:
            new[a] += nota
            conta[a] += 1
        else:
            new[a] = nota
            conta[a] = 1
    for letra in new:
        new[letra] = new[letra]/conta[letra]
    return new


         