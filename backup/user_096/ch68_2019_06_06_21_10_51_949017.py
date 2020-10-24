def separa_trios(lista_a):
    saida = []
    i = 0
    b=3
    while i < len(lista_a):
        trio = lista_a[i:b]
        saida.append(trio)
        b += 3
        i += 3
    return saida
