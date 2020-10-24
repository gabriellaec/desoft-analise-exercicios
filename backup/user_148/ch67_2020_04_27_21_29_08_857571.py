def alunos_impares(nomes):
    lista = []
    if len(nomes) == 1:
        lista.append(nomes)
    else:
        lista.append(nomes[1::2])
    return lista
