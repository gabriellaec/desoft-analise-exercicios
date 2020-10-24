def separa_trios(alunos):
    trios = []
    i = 0
    while i in range(len(alunos) - 2):
        trios.append(['{0}', '{1}', '{2}'.format(aluno[i], aluno[i+1], aluno[i+2])])
        i += 3
    return trios