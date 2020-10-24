def junta_nome_sobrenome(lista1, lista2):
    lista3 = []
    for i in range(len(lista1)):
        k = lista1[i] + ' ' + lista2[i]
        lista3.append(k)
    return lista3