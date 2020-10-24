def medias_por_inicial (dicionario):
    dic1 = {}
    dic2 = {}
    for aluno,nota in dicio.items():
        if aluno[0] in dic1:
            dic1[aluno[0]][0] += nota
            dic1[aluno[0]][1] += 1
        else:
            dic1[aluno[0]] = [nota,1]
            
    