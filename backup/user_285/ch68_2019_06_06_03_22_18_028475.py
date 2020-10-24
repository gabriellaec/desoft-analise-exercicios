def separa_trios(alunos):
    listatrios=[]
    contador=0
    contador2=3
    while contador<len(alunos):
        listatrios.append(alunos[contador:contador2])
        contador+=3
        contador2+=3
    return listatrios