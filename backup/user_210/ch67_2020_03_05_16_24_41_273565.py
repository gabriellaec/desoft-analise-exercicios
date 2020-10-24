def alunos_impares(lista):
    l = []
    for c in range(len(lista)):
        if c % 2 != 0:
        	l.append(l[c])
    return l