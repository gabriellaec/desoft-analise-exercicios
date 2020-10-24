def alunos_impares(nomes):
    lista = []
    i = 0
    while i<len(nomes):
        if i % 2 == 1:
            lista.append(nomes[i])
    return lista
