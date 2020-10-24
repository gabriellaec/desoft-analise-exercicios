def medias_por_inicial(x):
    dicionario = {}
    for nome in x.keys():
        for letra in nome:
            if letra == nome[0]:
                dicionario[letra] += nome
    return dicionario