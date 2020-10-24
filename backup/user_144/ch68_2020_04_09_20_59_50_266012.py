def separa_trios(alunos):
    trio1 = []
    for i in range(len(alunos)):
        if alunos[:3] not in trio1:
            trio1.append(alunos[:3])
          

    return trio1