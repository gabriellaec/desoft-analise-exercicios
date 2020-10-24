def alunos_impares(alunos):
    lista_alunos_impares=[]
    for i in range(len(alunos)):
        if alunos[i] % 2 != 0:
        lista_alunos_impares.append(alunos[i]) 
    return lista_alunos_impares
            