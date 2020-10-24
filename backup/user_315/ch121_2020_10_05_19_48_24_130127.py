def subtracao_de_listas(lista1, lista2):
    lista_final = []
    i = 0
    while i < len(lista1) or i < len(lista2):
        if lista2 [i] != lista1 [i]:
            lista_final.append (lista1[i])
        i += 1

    return lista_final