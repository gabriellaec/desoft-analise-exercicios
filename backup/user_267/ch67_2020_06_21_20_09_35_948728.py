def alunos_impares(lista_alunos):
    lista_impares = []
    for i in range(len(lista_alunos)):
        if i%2 != 0:
            lista_impares.append(lista_alunos[i])
    return lista_impares
        
        