def alunos_impares(lista):
    alunosi = []
    for i,e in enumerate(lista):
        if i%2 != 0:
            alunosi.append(e)
    return alunosi