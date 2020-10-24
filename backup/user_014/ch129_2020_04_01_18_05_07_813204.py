def verifica_quadrado_perfeito (n):
    b = 0
    while n > b:
        n = n - (2 * b + 1)
        b += 1
        if n == 0:
            return True
        else:
            return False