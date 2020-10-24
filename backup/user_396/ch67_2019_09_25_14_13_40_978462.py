def alunos_impares(x):
    lis = []
    i = 0
    while i < len(x):
        lis.append(x[i+1])
        i += 1
    return lis
    