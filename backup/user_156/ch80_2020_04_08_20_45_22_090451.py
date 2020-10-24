def interseccao_chaves(dicionario1, dicionario2):
    saida = []

    dic1 = dicionario1.keys()
    dic2 = dicionario2.keys()

    for element in dic1:
        if element in dic2:
            saida.append(element)

    return saida
        