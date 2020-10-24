def separa_trios(alunos):
    n=len(alunos)
    i=0
    j=1
    k=2
    while n>=3:
        ",".join(alunos[i], alunos[j], alunos[k])
        i+=3
        j+=3
        k+=3
        n=n-3
    if n==2:
        ",".join(alunos[-2], alunos[-1]
    return alunos    