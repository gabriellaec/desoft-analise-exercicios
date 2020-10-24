def alunos_impares(nomes):
    impares = []
    i = 0
    while i < len(nomes):
        if i % 2 !=0:
            impares.append(nomes[i])
        i += 1
    return impares