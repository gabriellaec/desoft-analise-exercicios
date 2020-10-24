def alunos_impares(lista_alunos):
    lista_alunos = []
    alunos_impares = []
    i = 0
    n = len(lista_alunos)
    while i < n:
        if i%2 != 0:
            alunos_impares.append(lista_alunos[i])
        i += 1
    return alunos_impares
    