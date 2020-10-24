def separa_trios(alunos):
    return [alunos[i:i+3]for in range(len(alunos)/3+ 1*(len(alunos)%3 == 0) )]