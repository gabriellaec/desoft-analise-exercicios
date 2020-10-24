def alunos_impares(lista_alunos):
    impares = []
    i = 0
    while i < len(lista_alunos):
        if(i%2!=0):
            impares.append(lista_alunos[i])
        i = i +1
    return impares