def alunos_impares(l):
    newl = []
    i = 0
    for t in l :
        if i % 2 != 0:
            newl.append(t)
        i+=1
    return newl