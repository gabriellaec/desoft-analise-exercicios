def medias_por_inicial(dicionario):
    dic = {}
    lista = list(dicionario.keys())
    for nome in lista:
        inicial = nome[0]
        soma = 0
        qnt = 0
        for nome in lista:
            if inicial == nome[0]:
                qnt += 1
                soma += dicionario[nome]
        media = soma/qnt
        dic[inicial] = media
    return dic
        