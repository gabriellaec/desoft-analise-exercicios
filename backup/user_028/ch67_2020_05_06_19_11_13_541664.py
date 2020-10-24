def alunos_impares(nomes):
    i = 0
    impares = []
    while i < len(nomes):
        if i %2 != 0:
            impares.append(nomes[i])
    return impares        
           