def monta_mala(lista_p):
    tot =0
    i = 0
    while i < len(lista_p):
        tot += lista_p[i]
        if tot > 23:
            lista_p = lista_p[:i]
            break
        i += 1
    return pesos