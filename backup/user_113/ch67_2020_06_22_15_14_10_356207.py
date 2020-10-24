def alunos_impares(alunos):
    alunos_imp = []
    for i in range(0, len(alunos)):
        alunos_imp += alunos[i+2]
    return alunos_imp