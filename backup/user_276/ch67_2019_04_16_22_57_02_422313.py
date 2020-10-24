def alunos_impares(lista):
    listaimpares = []
    i = 0
    while i < len(lista):
        if i%2 != 0:
            listaimpares.append(lista[i])
        