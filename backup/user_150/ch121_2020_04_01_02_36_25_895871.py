def subtracao_de_listas(lista1, lista2):
    lista3 = []
    l1_counter = 0
    while l1_counter < len(lista1):
        if lista1[l1_counter] not in lista2:
            lista3.append(lista1[l1_counter])
            l1_counter += 1
    return lista3