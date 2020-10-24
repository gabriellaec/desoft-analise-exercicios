def medias_por_inicial (alunos_notas):
    alunos_notas = dict()
    iniciais_médias = dict()
    for i in alunos_notas:
        if i[0] not in iniciais_médias:
            iniciais_médias[i] == alunos_notas[i]
        else:
            iniciais_médias[i] = (iniciais_médias[i]+alunos_notas[i])/2
    return iniciais_médias