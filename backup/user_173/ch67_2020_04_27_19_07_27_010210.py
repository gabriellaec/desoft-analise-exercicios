def alunos_impares(lista1):
    lista2 = []
    i = 0
    while i < len(lista1):
        if i%2 != 0:
            lista2.append(lista1[i])
    return lista2