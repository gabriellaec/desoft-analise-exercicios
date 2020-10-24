def calcula_media(lista):
    n = 0
    for i in range (len(lista)):
        n = n + len(lista[i])
    soma = 0
    for dic in lista:
        for nota in dic.values():
            soma = soma + nota
    media = soma/n
    return media