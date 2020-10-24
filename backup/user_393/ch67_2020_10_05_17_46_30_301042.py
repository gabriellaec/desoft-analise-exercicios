def alunos_impares(lista):
    lista_alunos_impares= []
    i= 0
    while i < len(lista):
        if i%2 != 0:
            lista_alunos_impares.append(lista[i])
            i= i + 1
        else:
            i= i + 1
    return lista_alunos_impares