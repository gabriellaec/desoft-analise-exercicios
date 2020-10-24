def estritamente_crescente(lista):
    saida = [lista[0]]
    for e in lista:
        if e > saida[-1]:
            saida.append(e)
    return saida