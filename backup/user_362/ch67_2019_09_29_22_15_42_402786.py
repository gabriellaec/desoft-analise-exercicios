def alunos_impares(lista_alunos):
    lista_impares=[]
    for i in range(1,len(lista_alunos),2):
        lista_impares.append(lista_alunos[i])
    return lista_impares
    