def alunos_impares(lista):
    impar = []
    e = 0
    while e < len(lista):
        if e % 2 != 0:
            impar.append(lista[e])
            e += 1
        else:
            e += 1
    return impar