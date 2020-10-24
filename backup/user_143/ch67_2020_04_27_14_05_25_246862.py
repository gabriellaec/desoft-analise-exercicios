def alunos_impares(l):
    li=[]
    for i in range(len(l)):
        p=l[::2]
        li.append(p)
    return li
        