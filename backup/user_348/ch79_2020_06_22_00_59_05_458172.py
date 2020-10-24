def monta_dicionario(lista1, lista2):
    # cria um dicionário vazio
    dicionario = {}
    # condição
    for i in range(len(lista1)):
        # determina que o elemento do índice atual da lista1 será a chave e o da lista2 o valor
        dicionario[lista1[i]] = lista2[i]
    return dicionario