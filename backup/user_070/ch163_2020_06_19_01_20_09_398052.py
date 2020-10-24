def calcula_media(ano):
    soma = 0
    alunos = 0
    for turma in ano:
        for nota in turma.values():
            soma += nota
            alunos += 1
    return soma/alunos