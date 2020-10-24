def separa_trios(lista_alunos):
    trios = []
    i = 0
    while i < len(lista_alunos):
        if i %3 == 0:
            trio = []
            trio.append(lista_alunos[i])
            trios.append(trio)
        else:
            trio.append(lista_alunos[i])
        i += 1
    return trios
