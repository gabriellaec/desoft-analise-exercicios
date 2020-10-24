def subtracao_de_listas (lista1, lista2):

    lista_final = []
    if lista2 == []:
        return lista1

    for item1 in lista1:
        for item2 in lista2:
            if item1 == item2:
                lista_final.append(item1)

    return lista_final