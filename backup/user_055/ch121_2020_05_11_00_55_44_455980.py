def subtracao_de_listas(lista_1, lista_2):
    not_in_lista = []
    for element in lista_1:
        if element not in lista_2:
            not_in_lista.append(element)
    return not_in_lista