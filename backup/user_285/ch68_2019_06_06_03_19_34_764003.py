def separa_trios(alunos):
    listatrios=[]
    contador=0
    while contador<len(alunos):
        listatrios.append(alunos[:3])
        contador+=3
    return listatrios