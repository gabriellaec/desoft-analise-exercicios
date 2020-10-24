def alunos_impares(lista):
    listaimpares = []
    for i in lista:
        if (-1)**i != 1:
            listaimpares.append(i)
    return listaimpares    