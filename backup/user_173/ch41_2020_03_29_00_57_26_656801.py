def zera_negativos (valores):
    novos_valores = valores
    i = 0
    while i < len(valores) -1:
        if novos_valores [i] < 0:
            novos_valores [i] = 0
        i += 1
    return novos_valores