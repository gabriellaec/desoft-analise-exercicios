def separa_trios (alunos):
    trios=[]
    inicio=list(range(0,len(alunos),3))
    for i in inicio:
        if i!=inicio[-1]:
            trio=alunos[i:inicio[i+1]]
            trios.append (trio)
        else:
            trios.append (alunos[i:])
    return trios