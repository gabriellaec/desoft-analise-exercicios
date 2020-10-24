def alunos_impares(alunos):
    i = 1
    alunos_imp = []
    while i < len(alunos):
        alunos_imp.append(alunos[i])
        i += 2
    return alunos_imp