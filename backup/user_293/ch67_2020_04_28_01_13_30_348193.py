def alunos_impares(lista_nome):
    lista_impar = []
    i = 0
    for e in lista_nome:
        if i%2 != 0:
            lista_impar.append(e)
        i += 1
    return lista_impar