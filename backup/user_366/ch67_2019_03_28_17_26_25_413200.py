def alunos_impares(alunos):
    i = 0
    while i < len(alunos):
        if i % 2 == 0:
            del alunos[i]
        i += 1
    return alunos