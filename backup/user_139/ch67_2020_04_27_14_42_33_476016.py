def alunos_impares(lista_nomes):
    lista = []
    if len(lista_nomes) < 2:
        return []
    else:
        lista.append(lista_nomes[1::2])
    return lista