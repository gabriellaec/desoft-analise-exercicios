def alunos_impares(alunos):
    lista_impares = []
    i = 1
    while i < len(alunos):
        lista_impares.append(alunos[i])
        i += 2
    return lista_impares