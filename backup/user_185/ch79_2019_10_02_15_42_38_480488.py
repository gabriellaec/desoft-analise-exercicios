def monta_dicionario(lista_1 , lista_2):
    i = 0
    dicio = {}
    if len(lista_1) == len(lista_2):
        while i < len(lista_2):
            chave = lista_1[i]
            valor = lista_2[i]
            dicio[chave] = valor
            i = i + 1
    return dicio