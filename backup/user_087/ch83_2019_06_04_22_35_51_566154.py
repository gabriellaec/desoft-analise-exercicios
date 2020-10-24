def medias_por_inicial(dicionario_notas):
    letra_media = dict()
    contador = 1
    soma = 0
    for nome in dicionario_notas:
        if nome[0] not in letra_media:
            soma += dicionario_notas[nome]
            contador += 1
        else: 
            soma = dicionario_notas[nome]
            contador = 1
        letra_media[nome[0]] = soma/contador
        return letra_media
        