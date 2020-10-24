def subtracao_de_listas(lista1, lista2):
    subtracao = []
    for elemento1 in lista1:
        if elemento1 not in lista2:
            subtracao.append(elemento1)
    return subtracao