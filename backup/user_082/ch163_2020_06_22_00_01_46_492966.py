def calcula_media(lista):
    nota_turmas = 0
    quantidade_alunos = 0
    media_turmas = 0
    for dic in lista:
        for aluno in dic:
            nota_turmas += dic[aluno]
            quantidade_alunos += 1

    media_turmas = nota_turmas / quantidade_alunos
    return media_turmas
