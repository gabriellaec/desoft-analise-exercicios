def separa_trios(alunos):
    listatrios=[]
    for i in range(len(alunos)):
        listatrios.append(alunos[:3+i])
    return listatrios