def separa_trios(alunos):
    listatrios=[]
    for i in range(len(alunos)):
        trio=[alunos[i],alunos[i+1],alunos[i+1]]
        listatrios.append(trio)