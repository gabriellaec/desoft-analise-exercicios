def conta_a (estringui):
    i = 0
    contador = 0
    while (i < len(estringui)):
        if (estringui[i] == "a"):
            contador = contador + 1
        i = i + 1
    return contador