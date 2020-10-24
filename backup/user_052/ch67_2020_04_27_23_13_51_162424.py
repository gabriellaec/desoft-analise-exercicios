def alunos_impares (listanomes):
    listaimpares = []
    i = 1
    while i < len(listanomes):
        listaimpares.append(listanomes[i])
        i += 2
    return listaimpares