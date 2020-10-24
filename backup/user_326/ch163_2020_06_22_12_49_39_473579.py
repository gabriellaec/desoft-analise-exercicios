def calcula_media(alunos):
    soma = 0
    iteracao = 0
    for dicionario in alunos:
        for nota in dicionario.values():
            soma += nota
            iteracao += 1
    media = soma/iteracao
    return media