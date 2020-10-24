def separa_trios(alunos):
    n=len(alunos)
    trios=[]
    i=0
    j=1
    k=2
    while n>=3:
        trios.append([alunos[i], alunos[j], alunos[k]])
        i+=3
        j+=3
        k+=3
        n=n-3
    if n==2:
        trios.append([alunos[-2], alunos[-1]])
    elif n==1:
        trios.append(trios[-1])
    return trios 