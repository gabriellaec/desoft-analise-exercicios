def alunos_impares(l1):
    l2=[]
    for i in range(len(l1)):
        if i%2!=0:
            l2.append(l1[i])
    return l2
    