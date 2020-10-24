def junta_nome_sobrenome(lista_1,lista_2):
    lista_3 = []
    for i in zip(lista_1, lista_2):
        lista_3.append(i[0] +i[1])
    return lista_3