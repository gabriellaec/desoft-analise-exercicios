def alunos_impares(lista_nomes):
    lista_impares = []
    for e in range len(lista_nomes):
        if lista_nomes[e] %2 !=0:
            lista_impares.append(lista_nomes[e])
    return lista_impares