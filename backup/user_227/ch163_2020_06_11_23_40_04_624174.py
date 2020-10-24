def calcula_media(lista):

    notas = []
    for dicionario in lista:
        for chave in dicionario:
            notas.append(dicionario[chave])

    media = (sum(notas))/(len(notas))

    return media