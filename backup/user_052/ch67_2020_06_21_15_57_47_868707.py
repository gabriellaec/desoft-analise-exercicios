def alunos_impares (lista_nome):
    nova = []
    i = 0
    while i < len(lista_nome):
        if i % 2 != 0:
            nova.append(lista_nome[i])
            i += 1
        else:
            i += 1
    return nova