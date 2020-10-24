def medias_por_inicial(dicionario):
    iniciais = {}
    denominadores = {}
    for nome,nota in dicionario.items():
        if nome[0] not in iniciais:
            iniciais[nome[0]] = nota
            denominadores[nome[0]] = 1
        else:
            iniciais[nome[0]] += nota
            denominadores[nome[0]] += 1
    for letra in iniciais.keys():
        iniciais[letra] /= denominadores[letra]
    return iniciais