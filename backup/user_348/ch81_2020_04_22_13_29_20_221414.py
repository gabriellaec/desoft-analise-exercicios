def interseccao_valores (dicionario_1, dicionario_2):
    lista = []
    for a in dicionario_1.values():
        if a in dicionario_2.values():
            lista.append(a)
    return lista
            