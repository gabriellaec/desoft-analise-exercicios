def calcula_media(turmas):
    soma = 0
    qntd = 0
    for i in turmas:
        for x in i:
            soma += x
            qntd += 1
    media = soma / qntd
    return media