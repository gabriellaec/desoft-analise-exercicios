def separa_trios(alunos):
    i=0
    j=1
    k=2
    lista=[]
    while i<len(alunos):
        ",".join(alunos[i], alunos[j], alunos[k])
        i+=3
        j+=3
        k+=3
    return lista    