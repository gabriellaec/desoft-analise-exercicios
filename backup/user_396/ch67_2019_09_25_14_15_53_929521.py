def alunos_impares(x):
    lis = []
    i = 0
    while i < len(x):
        if i % 2 != 0:
        	lis.append(x[i])
        i += 1
    return lis
    