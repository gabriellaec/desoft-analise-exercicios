def alunos_impares(lista):
    impar = []
    
    for e in len(lista):
        if e % 2 != 0:
            impar.append(lista[e])
    return impar