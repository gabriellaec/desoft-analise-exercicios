def junta_nome_sobrenome(lista_1,lista_2):
    lista_3 = []
    espaco = " "
    for i, n in zip(lista_1, lista_2):
        lista_3.append(i + espaco + n)
    return lista_3