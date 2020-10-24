def interseccao_chaves(dict_1, dict_2):
    keys_1 = dict_1.keys()
    keys_2 = dict_2.keys()
    lista_keys = []
    for i in keys_1 and i in keys_2:
        if i in keys_1 and i in keys_2:
            lista_keys.append(i)
    return lista_keys
    