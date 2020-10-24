def alunos_impares(lalunos):
    listaimpares = []
    i = 0
    while i < len(lalunos):
        if i%2 != 0:
            listaimpares.append(lalunos[i])
            i += 1
        else:
            i += 1
    return listaimpares