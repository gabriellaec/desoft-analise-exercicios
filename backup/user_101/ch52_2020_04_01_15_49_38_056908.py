def calcula_total_da_nota(l1, l2):
    i = 0
    listaF = [0] * len(l1)
    while i < len(listaF):
        listaF[i] = l1[i] * l2[i]
        i += 1
    precoF = sum(listaF)
    return precoF