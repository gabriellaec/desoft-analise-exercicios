def separa_trios(total_alunos):
    trios = []
    i = 0
    while i < len(total_alunos):
        a = total_alunos[i:i+3]
        trios.append(a)
        i += 3
    return trios