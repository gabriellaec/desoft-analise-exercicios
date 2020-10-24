def alunos_impares(x):
    i = 0
    L = []
    while i < len(x):
        if i % 2 != 0:
            L.append(x[i])
        i += 1