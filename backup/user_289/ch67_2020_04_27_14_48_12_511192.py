def alunos_impares(lista_nomes):
    lista_impares = []
    e = 0
    while e < len(lista_nomes):
        if lista_nomes[e] %2 !=0:
            lista_impares.append(lista_nomes[e])
            e += 1
        else:
            e += 1
    return lista_impares