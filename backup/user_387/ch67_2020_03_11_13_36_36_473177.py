def alunos_impares(a):
    p=[]
    for ele in range(len(a)):
        if ele%2 != 0:
            p.append(a[ele])
    return(p)