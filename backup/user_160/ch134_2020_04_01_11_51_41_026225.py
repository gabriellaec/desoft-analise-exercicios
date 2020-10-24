def verifica_quadrado_perfeito (n):
    i = 2
    while i >= n/2:
        n -= i
        i = i + 2
    if n == n/2:
        return ("True")
    else:
        return ("False")
    