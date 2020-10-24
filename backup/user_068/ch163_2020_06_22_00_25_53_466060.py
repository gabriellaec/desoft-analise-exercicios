def calcula_media(alunos):
    media = 0
    soma = 0
    num = 0
    for dicionario in alunos:
        for valores in dicionario.values():
            soma += valores
            num += 1
        media = soma/num
    return media