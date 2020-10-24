def medias_por_inicial (notas):
    medias = {}
    contagem = {} 
    for nome in notas.keys():
        letra = nome[0]
        if letra not in medias.keys():
            medias[letra] = 0
            contagem[letra] = 0
        medias[letra] += notas[nome]
        contagem[letra] += 1
    for letra in medias.keys():
        medias[letra] = medias[letra]/contagem[letra]
    return medias
