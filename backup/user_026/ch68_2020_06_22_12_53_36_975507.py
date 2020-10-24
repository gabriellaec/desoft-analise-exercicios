def separa_trios(alunos):
    trios= []
    i= 0
    while i < len(alunos):
        trios.append(alunos[i:i+3])   #fatiamento
        i += 3
    return trios