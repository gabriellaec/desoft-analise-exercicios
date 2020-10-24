def verifica_quadrado_perfeito(n):
    i = 0
    while n > 0:
        n = n - (2i+1)
        i += 1
    if n == 0:
        return True
    else:
        return False