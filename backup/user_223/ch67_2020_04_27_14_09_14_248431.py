def alunos_impares(nomes_alunos):
    alunosimpares=[]
    if len(nomes_alunos) == 1:
            alunosimpares.append(nomes_alunos)
    else:
        alunosimpares.append(nomes_alunos[1: :2])
    return alunosimpares
        