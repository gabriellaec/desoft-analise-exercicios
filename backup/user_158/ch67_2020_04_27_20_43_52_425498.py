def alunos_impares(lista):
    impares = []
    for i in range(0,len(lista)):
        if i%2 !=0:
            impares.append(lista[i])
    return impares