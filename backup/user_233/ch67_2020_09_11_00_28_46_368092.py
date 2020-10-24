def alunos_impares(alunos):
    
    impares = list()
    adicionar = True
    
    for aluno in alunos[1:]:
        if adicionar: impares.append(alunos)
        adicionar = not adicionar
    
    return impares