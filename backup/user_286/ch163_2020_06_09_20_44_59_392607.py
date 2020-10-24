def calcula_media(dicionarios):
    notas = 0
    alunos = 0
    for dic in dicionarios:
        notas += sum(dic.values())
        for aluno in dic:
            alunos += 1

    return notas / alunos