def conta_a (texto):
    contador1 = 0
    contador2 = 0
    n = len(texto)
    while contador1 < n:
        if texto[contador1] == "a":
            contador2 += 1
    contador1 += 1
    return contador1
        