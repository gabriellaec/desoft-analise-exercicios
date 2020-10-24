def medias_por_inicial(x):
    dicionario = {}
    divisor = [0]*len(x)
    for nome,nota in x.items():
        if nome[0] not in dicionario:
            dicionario[nome[0]] = nota
            divisor[nome[0]] = 1
        else:
            dicionario[nome[0]] += nota
            divisor[nome[0]] += 1
    for letra,total in dicionario.items:
        dicionario[letra] = total/divisor[letra]
    return dicionario