def alunos_impares(lista):
    i = 0
    i_impar = []
    while i < len(lista):
        if i%2 != 0:
            i_impar.append(lista[i])
        i += 1
    return i_impar