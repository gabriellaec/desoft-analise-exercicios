def separa_trios(alunos):
    return [alunos[i:i+3] for i in range(int(len(alunos)/3)+ 1* (not (len(alunos)%3 == 0)) )]


