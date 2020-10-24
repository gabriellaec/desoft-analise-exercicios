def calcula_media(alunos):
    soma = 0
    qnt = 0
    for i in range(len(alunos)):
        for v in i:
            soma+=v
            qnt+=1
            media = soma/qnt
    return media
            
        