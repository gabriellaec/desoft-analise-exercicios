def aluno_impares(x):
    l = []
    i = 0
    while i < len(x):
        if i%2 != 0:
            l.append(x[i])
        i+=1
    return l