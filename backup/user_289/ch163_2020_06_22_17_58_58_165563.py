def calcula_media(lista):
    notas_somadas = 0
    numero_alunos = 0
    for turma in lista:
        for nota in turma.values():
            notas_somadas += nota
            numero_alunos += 1
    media = notas_somadas/numero_alunos
    return media