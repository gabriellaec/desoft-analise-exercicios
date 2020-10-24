def alunos_impares(nomes_alunos):
    lista_impares = []
    a = nomes_alunos[1::2]
    lista_impares.append(a)
    lista_impares.append(nomes_alunos[0])
    return lista_impares
    