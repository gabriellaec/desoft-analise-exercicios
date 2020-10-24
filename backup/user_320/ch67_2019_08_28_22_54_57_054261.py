def alunos_impares(lista):
    cont = 0
    alunos = []
    while cont < len(lista):
        if cont % 2 != 0:
            alunos.append(lista[cont])
        cont += 1
    return alunos