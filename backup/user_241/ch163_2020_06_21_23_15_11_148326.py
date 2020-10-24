def calcula_media(alunos):
    soma = 0
    total = 0
    for dicionario in alunos:
        valores = dicionario.values()
        for nota in valores:
            soma += nota
            total += 1
    media = soma/total
    return media
    