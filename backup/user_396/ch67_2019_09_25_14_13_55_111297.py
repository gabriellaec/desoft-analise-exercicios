def alunos_impares(x):
    lis = []
    i = 0
    while i < len(x)-1:
        lis.append(x[i+1])
        i += 1
    return lis
    