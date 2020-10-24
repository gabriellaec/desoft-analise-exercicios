def separa_trios(lista_alunos):
    grupos = []
    for i in range(0, len(lista_alunos)):
        if i %3 == 0:
            trio = []
            trio.append(lista_alunos[i])
            grupos.append(trio)
        else:
            trio.append(lista_alunos[i])
    return grupos
