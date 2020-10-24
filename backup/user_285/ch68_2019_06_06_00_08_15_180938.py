def separa_trios(alunos):
    listatrios=[]
    for i in range(len(alunos)):
        if (i+2)%3==0:
            trio=[alunos[i], alunos[i+1], alunos[i+2]
            listatrios.append(trio)
        else:
            dupla=[alunos[i],alunos[i+1]]
            listatrios.append(dupla)