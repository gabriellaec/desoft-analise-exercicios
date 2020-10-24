def alunos_impares(alunos):
    
    impares = []
    numero_de_alunos = len(alunos)
    
    if numero_de_alunos % 2 != 0: numero_de_alunos += 1
        
    for numero in range(1, numero_de_alunos, 2):
        impares.append(alunos[numero])
        
    return impares
    
    