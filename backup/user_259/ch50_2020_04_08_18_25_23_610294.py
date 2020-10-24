def junta_nome_sobrenome(lista1, lista2):
    lista3 = []
    i = 0
    while (i<len(lista1)) and (i<len(lista2)):
        lista3[i] = '{0} {1}'.format(lista1[i], lista2[i])
    return lista3
                                     