def interseccao_chaves(dicionario1, dicionario2):
    lista_chaves = []
    lista_keys_1 = list(dicionario1.keys())
    lista_keys_2 = list(dicionario.keys())
    for i in lista_keys_1:
        if i in lista_keys_2:
            lista_chaves.append(i)
    return lista_chaves