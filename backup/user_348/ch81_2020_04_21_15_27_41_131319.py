def interseccao_valores (dicionario_1, dicionario_2):
    lista = []
    for v1 in dicionario_1.values() and v2 in dicionario_2.values():
        if v1 == v2:
            valor = v1
            lista.append(valor)
        return lista
            