def alunos_impares(lista):
    if len(lista) == 1:
        return lista
    else:
        impares = lista[::2]
        return impares
    