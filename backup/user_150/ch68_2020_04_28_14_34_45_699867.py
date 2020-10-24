def separa_trios(alunos):
    lista_trios = []
    i = 0
    f = 3
    if len(alunos) <= 2:
        lista_trios.append(alunos)
    while f <= len(alunos):
        lista_trios.append(alunos[i:f])
        i += 3
        f += 3
        if len(alunos[i:]) <= 2 and len(alunos[i:]) > 0:
            lista_trios.append(alunos[i:])
    return lista_trios
