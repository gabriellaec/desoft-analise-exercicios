def verifica_quadrado_perfeito(n):
    i = 1
    while i >= 1:
        n-=i
        i+=2
    if n == 0:
        return True
    elif n < 0:
        return False