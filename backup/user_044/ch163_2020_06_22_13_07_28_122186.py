def calcula_media(ls):
    notas = 0
    alunos = 0
    for turma in ls:
        for aluno in turma.values():
            notas += aluno
            alunos += 1
    notas = notas/alunos
    return notas
        