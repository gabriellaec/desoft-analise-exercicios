def alunos_impares(lista_nomes):
    lista_impares = []
    lista_pares = []
    i = 0
    while i < len(lista_nomes):
        fatia = lista_nomes[i]
        pos = lista_nomes.index(fatia)
        if pos % 2 == 0:
            lista_pares.append(fatia)
        elif pos % 2 != 0:
            lista_impares.append(fatia)
        i = i + 1
    return lista_impares
    