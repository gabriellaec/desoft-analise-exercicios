def separa_trios(alunos):
    return [alunos[i*3:i*3+3] for i in range(int(len(alunos)/3)+ 1* (not (len(alunos)%3 == 0)) )]




