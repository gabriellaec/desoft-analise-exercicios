def medias_por_inicial(x):
    dicionario = {}
    for nome,nota in x.items():
        if nome[0] not in dicionario:
            dicionario[nome[0]] = nota
            divisor = 1
        else:
            dicionario[nome[0]] += nota
            divisor += 1
    for letra,total in dicionario.items:
        dicionario[letra] = total/divisor
    return dicionario