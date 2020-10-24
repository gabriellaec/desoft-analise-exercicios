def calcula_media(alunos):
    qnt = 0
    valor = 0
    for dic in alunos:
        for c,v in dic.items():
            qnt += 1
            valor += v
    media = valor / qnt
    return media
            