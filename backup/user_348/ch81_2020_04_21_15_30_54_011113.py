def interseccao_valores (dicionario_1, dicionario_2):
    lista = []
    for a in dicionario_1.values() and dicionario_2.values():
        valor = a
        lista.append(valor)
    return lista
            