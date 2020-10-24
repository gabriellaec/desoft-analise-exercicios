def alunos_impares(nomes):
    impares = []
    for i in range(len(nomes)):
        if i % 2 != 0:
            impares.append(nomes[i])
    return impares