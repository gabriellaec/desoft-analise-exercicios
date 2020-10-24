def calcula_media(alunos):
    soma = 0
    qnt = 0
    for i in alunos:
        for v in i.values():
            soma+=v
            qnt+=1
    media = soma/qnt
    return media