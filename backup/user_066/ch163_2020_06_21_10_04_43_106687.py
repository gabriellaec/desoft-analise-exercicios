def calcula_media(lista):
    media_aluno = 0
    n_alunos = 0
    for i in lista:
        for j,k in i.items():
            media_aluno += k
        n_alunos += len(i)
    media = media_aluno/n_alunos
    print(media)
    return media