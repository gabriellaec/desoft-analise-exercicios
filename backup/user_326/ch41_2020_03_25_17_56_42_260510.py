def zera_negativos(lista):
    n_elementos = len(lista) -1
    bloco = 0
    while n_elementos >= 0:
        bloco = lista[n_elementos]
        if bloco < 0:
            lista[n_elementos] = 0
            n_elementos -= 1
        else:
            n_elementos -= 1
    return lista