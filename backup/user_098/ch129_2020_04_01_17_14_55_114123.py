def verifica_quadrado_perfeito(n):
    ni=1
    while True:
        n=n-ni
        ni+=2
        if n == 0:
            return True
        elif n <= 0:
            return False