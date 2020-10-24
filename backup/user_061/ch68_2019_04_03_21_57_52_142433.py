def separa_trios(lista_alunos):
    trio = [0]
    if lista_alunos % 3 != 0:
        trio[0] = (lista_alunos % 3)
    trio.append(lista_alunos[::3])
    return trio
    