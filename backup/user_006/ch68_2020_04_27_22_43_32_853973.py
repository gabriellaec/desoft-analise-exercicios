def separa_trios(alunos):
    n=len(alunos)
    trios=alunos  
    i=0
    j=1
    k=2
    while n>=3:
        trios.append([trios[i], trios[j], trios[k]])
        i+=3
        j+=3
        k+=3
        n=n-3
    if n==2:
        trios.append([trios[-2], trios[-1]])
               
    return trios 