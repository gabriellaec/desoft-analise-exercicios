def alunos_impares (alunos):
    impares = []
    i = 0
    while i < len(alunos):
        impares.append(alunos[i])
        i = i + 2
    return impares