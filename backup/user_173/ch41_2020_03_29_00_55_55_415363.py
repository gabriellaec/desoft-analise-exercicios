def zera_negativos (valores):
    novos_valores = valores
    i = 0
    while i < len(valores) -1:
        if valores [i] < 0:
            valores [i] = 0
    	i += 1
    return novos_valores