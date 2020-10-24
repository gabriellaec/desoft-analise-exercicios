def verifica_quadrado_perfeito(n):
    i = 1
    while i < n:
        n -= i
        i += 2
    if n == 0:
        return True
    else:
        return False