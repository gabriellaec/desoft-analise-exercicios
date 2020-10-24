def alunos_impares(l):
    nl = []
    for i in range(len(l)):
        if i%2 != 0:
            nl.append(l[i])
    return nl