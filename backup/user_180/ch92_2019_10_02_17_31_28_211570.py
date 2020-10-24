def simplifica_dict(dicionario):
    lista_chaves_valores = []
    for key, value in dicionario.items():
        if key not in lista_chaves_valores:
            lista_chaves_valores.append(key)
        if value not in lista_chaves_valores:
            lista_chaves_valores.append(value)
    return lista_chaves_valores