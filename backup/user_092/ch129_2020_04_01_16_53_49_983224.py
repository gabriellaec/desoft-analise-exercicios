def verifica_quadrado_perfeito(n):
    s = 1
    g = n
    while(g > 0):
        g = g - s
        s += 2
    if g == 0:
        return True
    else:
        return False