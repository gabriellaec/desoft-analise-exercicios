def separa_trios(alunos):
    trios=[]
    i=1
    if len(alunos)%3==0:
        while i<len(alunos):
            trios.append(alunos[i:i+3])
            i+=3
    elif len(alunos)%3==2:
        while i<(len(alunos)-2):
            trios.append(alunos[i:i+3])
            i+=3
        trios.append(alunos[(len(alunos)-2):len(alunos)])
    elif len(alunos)%3==1:
        while i<(len(alunos)-1):
            trios.append(alunos[i:i+3])
            i+=3
        trios.append(alunos[(len(alunos)-1)])
    return trios 