def junta_listas(lista):
    saida = list()
    for e in lista:
        for i in range(len(e)):
            saida.append(e[i])
    return saida