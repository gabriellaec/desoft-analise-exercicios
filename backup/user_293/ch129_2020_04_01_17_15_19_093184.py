def verifica_quadrado_perfeito(n):
    i = 1
    while n >= 0:
        impar = i%2
        if impar != 0:
            n = n - i
            if n == 0:
                return True
            elif n < 0:
                return False
        i += 1