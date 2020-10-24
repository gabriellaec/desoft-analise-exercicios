def subtracao_de_listas (lista1, lista2):

    lista_final = []
    for item1 in range(len(lista1)):
        for item2 in range(len(lista2)):
            if item1 != item2:
                lista_final.append(item1)

    return lista_final