def alunos_impares(lista):
    lista_impares = []
    for i in range(len(lista)):
        if i % 2 == 1:
            lista_impares.append(lista[i])
    return lista_impares