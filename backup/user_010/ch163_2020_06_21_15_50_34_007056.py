def calcula_media (lista):
    snota=0
    alunos=0
    for dic in lista:
        for nota in dic.values():
            snota+=nota
            alunos+=1
    media=snota/alunos
    return media