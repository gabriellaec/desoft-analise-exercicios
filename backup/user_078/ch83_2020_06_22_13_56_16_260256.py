def medias_por_inicial(dicio):
    dicio1 = {}
    dicio2 = {}
    for aluno, nota in dicio.items():
        if aluno[0] in dicio1:
            dicio1[aluno[0]][0] += nota
            dicio1[aluno[0]][1] += 1
        else:
            dicio1[aluno[0]] = [nota, 1]
    for inicial, lista in dicio1.items():
        dicio2[inicial] = lista[0]/lista[1]
    return dicio2