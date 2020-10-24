def alunos_impares(alunos):
    lista_impares = []
    if len(alunos) == 1:
        return None
    else:
        for nomes in range(0, 1):
            lista_impares.append(alunos[1:: 2])
        return lista_impares