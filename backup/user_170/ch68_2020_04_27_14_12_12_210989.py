def separa_trios(alunos):
    i = 0
    trios = []
    while i < (len(alunos)-3):
        trios.append([alunos[i], alunos[i+1], alunos[i+2])
        i += 3
    return trios
        