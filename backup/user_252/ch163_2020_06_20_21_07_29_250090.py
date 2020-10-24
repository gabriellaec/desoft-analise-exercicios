def calcula_media(alunos):
    n=0
    x=0
    for turma in alunos:
        for classe in turma:
            l=turma[classe]
            n+=l
            x+=1
    media=(n/x)
    return media 