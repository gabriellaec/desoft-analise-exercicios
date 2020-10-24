def estritamente_crescente(lista):
    saida = []
    if len(saida) > 0:
        saida.append(lista[0])
        for e in lista:
            if e > saida[-1]:
                saida.append(e)
    return saida