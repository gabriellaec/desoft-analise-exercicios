def subtracao_de_listas(lista1, lista2):
    l_dif = []
    t = 0
    while t < len(lista2):
        if lista1[t] not in lista2:
            l_dif.append(lista1[t])
        t += 1
    return l_dif