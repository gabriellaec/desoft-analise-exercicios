def subtracao_de_listas (lista1, lista2):

    lista_final = []
    for item1 in range(lista1):
        for item2 in range(lista2):
            if not item1 in lista2:
                lista_final.append(item1)

    return lista_final