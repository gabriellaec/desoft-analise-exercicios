def alunos_impares(alunos):
    i = 0
    new = []
    while i < len(alunos):
        if i % 2 != 0:
            new.append(alunos[i])
        i += 1
    return new