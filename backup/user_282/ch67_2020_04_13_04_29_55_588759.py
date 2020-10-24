def alunos_impares(lista):
    if len(lista)%2 == 0:
        impar = lista[::2]
        return impar
    else:
        return lista