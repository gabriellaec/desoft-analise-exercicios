def calcula_media(ls):
    notas = 0
    turmas = []
    for turma in ls:
        for alunos in turma.values():
            notas += alunos
        notas = notas/len(turma)
        turmas.append(notas)
    notas = 0
    for i in turmas:
        notas += i
    notas = notas/len(turmas)
    return notas
        