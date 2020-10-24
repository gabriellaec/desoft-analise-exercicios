def alunos_impares(lista_nomes):
    if lista_nomes < 1:
        return []
    lista = []
    lista.append(lista_nomes[1::2])
    return lista