def verifica_quadrado_perfeito(n):
    i = 1
    roda = True
    while roda:
        n -= i
        i += 2
        if n<0:
            return False
            roda = False
        elif n == 0:
            return True
            roda = False