def interseccao_valores (dicionario_1, dicionario_2):
    lista = []
    for a in dicionario_1.values() and b in dicionario_2.values():
        if a == b:
            valor = a
            lista.append(valor)
        return lista
            