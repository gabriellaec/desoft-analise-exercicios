def separa_trios(alunos):
    trios = []
    trio = []
    i = 0
    while i in range(len(alunos) - 1):
        trio.append(alunos[i])
        trio.append(alunos[i+1])
        trio.append(alunos[i+2])
        trios.append(trio)
        i += 3
        trio = []
    return trios