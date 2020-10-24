def alunos_impares(nomes_alunos):
    alunosimpares=[]
    if len(nomes_alunos) == 1:
        alunosimpares.append("None")
    else:
        alunosimpares.append(nomes_alunos[1: :2])
    return alunosimpares
        