def separa_trios(alunos):
    trios = []
    trio = []
    i = 0
    while i < (len(alunos)):
        trio = alunos[i:i+3]
        trios.append(trio)
        trio = []
        i += 3
    return trios