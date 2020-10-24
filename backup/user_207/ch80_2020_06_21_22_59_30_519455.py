def interseccao_chaves(dicio1, dicio2):
    lista_keys = []
    for key in dicio1:
        if key in dicio2:
            lista_keys.append(key)
    return lista_keys