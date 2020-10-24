def subtracao_de_listas(lista1, lista2):
    l_dif = []
    t = 0
    while t < len(lista1):
        if lista2 == []:
            l_dif.append(lista1[t])
        elif lista1[t] not in lista2:
            l_dif.append(lista1[t])
        t += 1
    return l_dif