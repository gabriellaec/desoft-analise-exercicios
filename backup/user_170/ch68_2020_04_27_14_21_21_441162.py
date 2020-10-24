def separa_trios(alunos):
    trios =[]
    for i in range(0, len(alunos), 3):
        trios.append(alunos[i:i+3])
    return trios
        