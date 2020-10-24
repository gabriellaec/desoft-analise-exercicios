def separa_trios(total_alunos):
    trios = []
    i = 0
    while i < len(total_alunos):
        a = total_alunos[i:i+2]
        trios.append(a)
        i += 1
    return trios