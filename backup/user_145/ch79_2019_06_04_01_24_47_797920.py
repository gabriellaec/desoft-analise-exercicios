def monta_dicionario(lista_1, lista_2):
    dicionario = {}
    for letra in lista_2:
        for numero in lista_1:
            dicionario[letra] = numero
    return dicionario
